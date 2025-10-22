from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from textwrap import shorten
from typing import Iterable, List, Dict, Optional, Tuple
import logging
from docutils import nodes
from docutils.core import publish_doctree


# ------------------------------ Model -----------------------------------------
@dataclass(frozen=True)
class Article:
    filename: str
    title: str
    date: datetime
    keywords: List[str]
    description: str

    @property
    def datef(self) -> str:
        return self.date.strftime("%d %b %Y")

    def summary(self, width: int = 140) -> str:
        return shorten(self.description, width=width, placeholder="...")

    @property
    def link(self) -> str:
        # assumes files live in latest_news/
        return f"latest_news/{self.filename}"


# ------------------------------ Parsing ---------------------------------------


def _first_nonempty_paragraph(doc: nodes.document) -> Optional[str]:
    p = doc.next_node(nodes.paragraph)
    return p.astext().strip() if p else None


def _meta(doc: nodes.document) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for m in doc.findall(nodes.meta):
        name = (m.get("name") or "").strip().lower()
        val = (m.get("content") or "").strip()
        if name and val:
            out[name] = val
    return out


def parse_article(path: Path) -> Article:
    doc = publish_doctree(path.read_text(encoding="utf-8"))
    meta = _meta(doc)

    title = meta.get("title")

    date_raw = meta.get("date")

    date = datetime.strptime(date_raw, "%d-%m-%Y")

    kw = [t.strip() for t in (meta.get("keywords", "")).split(",") if t.strip()]

    desc = _first_nonempty_paragraph(doc) or ""

    return Article(
        filename=path.stem, title=title, date=date, keywords=kw, description=desc
    )


# ------------------------------ Indexing (single pass) ------------------------
def build_index(
    dir_path: Path, keyword_filter: Optional[str] = None
) -> Tuple[List[Article], List[str]]:
    """Scan once; return (articles_sorted_desc_by_date, all_keywords_sorted)."""
    articles: List[Article] = []
    keywords_set = set()

    for p in sorted(dir_path.glob("*.rst")):
        try:
            a = parse_article(p)
        except Exception as e:
            logging.warning("[Latest News] Skipping %s: %s", p, e)
            continue

        if (keyword_filter is None) or (keyword_filter in a.keywords):
            articles.append(a)

        for kw in a.keywords:
            keywords_set.add(kw)

    articles.sort(key=lambda a: a.date, reverse=True)
    return articles, sorted(keywords_set)


# ------------------------------ Rendering -------------------------------------
def _indent(block: str, n: int) -> str:
    pad = " " * n
    return "\n".join(
        (pad + line) if line.strip() else "" for line in block.splitlines()
    )


def render_carousel(posts: Iterable[Article]) -> str:
    posts = list(posts)
    if not posts:
        return ".. note::\n   No news posts available.\n\n"

    lines = [".. card-carousel:: 3", ""]
    for a in posts:
        lines.append(
            f"""   .. card::
      :link: {a.link}
      :link-type: doc
      :shadow: none

      :fas:`calendar-alt` {a.datef}

      **{a.title}**

      {a.description}

""".rstrip()
        )
        lines.append("")  # blank line between cards
    return "\n".join(lines).rstrip() + "\n"


def render_tabset(dir_path: Path) -> str:
    all_posts, all_keywords = build_index(dir_path, keyword_filter=None)
    out = [".. tab-set::", "", "   .. tab-item:: All", "      :selected:", ""]
    out.append(_indent(render_carousel(all_posts), 6))

    # render each keyword tab with filtered posts without re-parsing
    # (we already have all posts; just filter in-memory)
    for kw in all_keywords:
        kw_posts = [a for a in all_posts if kw in a.keywords]
        out.extend([f"   .. tab-item:: {kw.title()}", ""])
        out.append(_indent(render_carousel(kw_posts), 6))

    return "\n".join(out) + "\n"


# ------------------------------ Sphinx hook -----------------------------------
def create_news_carousel(app) -> None:
    try:
        src = Path(app.srcdir)
        news_dir = src / "latest_news"
        out_dir = src / "_rst_includes"
        out_dir.mkdir(parents=True, exist_ok=True)

        (out_dir / "latest_news.rst").write_text(
            render_tabset(news_dir), encoding="utf-8"
        )
    except Exception as e:
        logging.warning("[Latest News] Failed to create news carousel: %s", e)
