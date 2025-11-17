from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from textwrap import indent, shorten
from typing import Iterable, List, Dict, Optional, Tuple
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
    priority: int = field(default=10)
    show_date: bool = field(default=True)

    @property
    def datef(self) -> str:
        return self.date.strftime("%d %b %Y")

    def summary(self, width: int = 140) -> str:
        return shorten(self.description, width=width, placeholder="...")

    @property
    def link(self) -> str:
        return f"/latest-news/{self.filename}"


# ------------------------------ Parsing ---------------------------------------

def _first_nonempty_paragraph(doc: nodes.document) -> Optional[str]:
    p = doc.next_node(nodes.paragraph)
    p = p.astext().strip()
    if p:
        p = p.split("\n\n")[0]
    p = " ".join(p.split("\n"))
    return p if p else None

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

    title = (meta.get("title") or path.stem).strip()
    priority = int(meta.get("priority", 10))
    show_date = meta.get("show-date", "true").strip().lower() != "false"

    date_raw = (meta.get("date") or "").strip()
    if not date_raw:
        raise ValueError(f"{path}: missing required 'date' meta")
    date = datetime.strptime(date_raw, "%d-%m-%Y")

    kw = [t.strip() for t in (meta.get("keywords", "")).split(",") if t.strip()]
    desc = _first_nonempty_paragraph(doc) or ""

    return Article(
        filename=path.stem, title=title, date=date, keywords=kw, description=desc,
        priority=priority, show_date=show_date
    )


# ------------------------------ Rendering -------------------------------------
def _indent(level: int) -> str:
    """Return indentation string for the given level (each level = 3 spaces)."""
    return " " * (level * 3)

EMPTY_NOTE = """\
.. note::
   No news posts available.

"""

CARD_TMPL_WITH_DATE = """\
.. card::
   :link: {link}
   :link-type: doc
   :shadow: none

   :fas:`calendar-alt` {datef}

   **{title}**

   {description}"""

CARD_TMPL_NO_DATE = """\
.. card::
   :link: {link}
   :link-type: doc
   :shadow: none

   **{title}**

   {description}"""

TABSET_HEADER = ".. tab-set::"

FIRST_TAB = """\
.. tab-item:: All
   :selected:"""

TAB_ITEM_TMPL = ".. tab-item:: {keyword}"

CAROUSEL_HEADER = ".. card-carousel:: 3"



def render_carousel(posts: Iterable[Article]) -> str:
    posts = list(posts)
    if not posts:
        return EMPTY_NOTE

    parts = [CAROUSEL_HEADER, ""]
    for a in posts:
        template = CARD_TMPL_WITH_DATE if a.show_date else CARD_TMPL_NO_DATE
        card = template.format(
            link=a.link, datef=a.datef, title=a.title, description=a.description
        )
        parts.append(indent(card, _indent(1)))

    return "\n\n".join(parts) + "\n"

def render_tabset(dir_path: Path) -> str:
    all_posts, all_keywords = build_index(dir_path, keyword_filter=None)

    title = """\
Latest News
-------------"""

    out: List[str] = [title, TABSET_HEADER]
    out.append(indent(FIRST_TAB, _indent(1)))
    out.append(indent(render_carousel(all_posts), _indent(2)))

    for kw in all_keywords:
        kw_posts = [a for a in all_posts if kw in a.keywords]
        tab_item = TAB_ITEM_TMPL.format(keyword=kw.title())
        out.append(indent(tab_item, _indent(1)))
        out.append(indent(render_carousel(kw_posts), _indent(2)))

    return "\n\n".join(out) + "\n"


# ------------------------------ Indexing (single pass) ------------------------
def build_index(
    dir_path: Path, keyword_filter: Optional[str] = None
) -> Tuple[List[Article], List[str]]:
    """Scan once; return (articles_sorted_desc_by_date, all_keywords_sorted)."""
    articles: List[Article] = []
    keywords_set = set()

    for p in sorted(dir_path.glob("*.rst")):
        a = parse_article(p)

        if (keyword_filter is None) or (keyword_filter in a.keywords):
            articles.append(a)
        keywords_set.update(a.keywords)

    articles.sort(key=lambda a: (a.priority, -a.date.timestamp()))
    return articles, sorted(keywords_set)


# ------------------------------ Sphinx hook -----------------------------------
def create_news_carousel(app) -> None:
    src = Path(app.srcdir)
    news_dir = src / "latest-news"
    out_dir = src / "_rst_includes"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "latest-news.rst").write_text(
        render_tabset(news_dir), encoding="utf-8"
    )
