from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from textwrap import dedent, indent, shorten
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
    priority: int

    @property
    def datef(self) -> str:
        return self.date.strftime("%d %b %Y")

    def summary(self, width: int = 140) -> str:
        return shorten(self.description, width=width, placeholder="...")

    @property
    def link(self) -> str:
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

    title = (meta.get("title") or path.stem).strip()

    priority = meta.get("priority")
    if priority and priority.strip():
        priority = int(priority)
    else:
        priority = 100

    date_raw = (meta.get("date") or "").strip()
    if not date_raw:
        raise ValueError(f"{path}: missing required 'date' meta")
    date = datetime.strptime(date_raw, "%d-%m-%Y")

    kw = [t.strip() for t in (meta.get("keywords", "")).split(",") if t.strip()]
    desc = _first_nonempty_paragraph(doc) or ""

    return Article(
        filename=path.stem, title=title, date=date, keywords=kw, description=desc, priority=priority
    )


# ------------------------------ Rendering -------------------------------------
IND_TAB = " " * 3
IND_CARD = " " * 6

EMPTY_NOTE = dedent("""\
.. note::
   No news posts available.

""")

CARD_TMPL = dedent("""\
.. card::
   :link: {link}
   :link-type: doc
   :shadow: none

   :fas:`calendar-alt` {datef}

   **{title}**

   {description}
""").rstrip()

TABSET_HEADER = dedent("""\
.. tab-set::
""").rstrip()

FIRST_TAB = dedent("""\
.. tab-item:: All
   :selected:
""").rstrip()

TAB_ITEM_TMPL = ".. tab-item:: {keyword}"

CAROUSEL_HEADER = dedent("""\
.. card-carousel:: 3
""").rstrip()



def render_carousel(posts: Iterable[Article]) -> str:
    posts = list(posts)
    if not posts:
        return EMPTY_NOTE

    parts = [CAROUSEL_HEADER, ""]
    for a in posts:
        card = CARD_TMPL.format(
            link=a.link, datef=a.datef, title=a.title, description=a.description
        )
        parts.append(indent(card, IND_TAB))

    return "\n\n".join(parts).rstrip() + "\n"

def render_tabset(dir_path: Path) -> str:
    all_posts, all_keywords = build_index(dir_path, keyword_filter=None)

    title = dedent("""\
Latest news
-------------
""").rstrip()

    out: List[str] = [title, TABSET_HEADER]
    out.append(indent(FIRST_TAB, IND_TAB))
    out.append(indent(render_carousel(all_posts), IND_CARD))

    for kw in all_keywords:
        kw_posts = [a for a in all_posts if kw in a.keywords]
        tab_item = TAB_ITEM_TMPL.format(keyword=kw.title())
        out.append(indent(tab_item, IND_TAB))
        out.append(indent(render_carousel(kw_posts), IND_CARD))

    return "\n\n".join(out).rstrip() + "\n"


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
    news_dir = src / "latest_news"
    out_dir = src / "_rst_includes"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "latest_news.rst").write_text(
        render_tabset(news_dir), encoding="utf-8"
    )
