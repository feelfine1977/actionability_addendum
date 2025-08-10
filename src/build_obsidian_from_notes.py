#!/usr/bin/env python3
"""
Obsidian Note Builder for Actionability Notes (HTML-safe)

Accepts either:
  - a single combined Markdown file, OR
  - a directory containing per-note .md and/or .html files

For HTML inputs, converts to Markdown-like text while PRESERVING <!--META_START--> ... <!--META_END-->
and normalizing headings to '# Paper Summary' / '## Section'.

Generates:
- One file per paper (YAML front matter + sections)
- Concept pages (CL/CR/FE/TI/EX/GA)
- Domain pages
- Global "Actionability Index.md"
- "See also" links via similarity of "How Actionability is Understood"
"""

import re
import os
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict

# ---- Similarity
try:
    from rapidfuzz import fuzz
    def str_sim(a: str, b: str) -> float:
        return fuzz.token_set_ratio(a or "", b or "") / 100.0
except Exception:
    from difflib import SequenceMatcher
    def str_sim(a: str, b: str) -> float:
        return SequenceMatcher(None, a or "", b or "").ratio()

# ---- HTML → Markdown-lite (preserve META comments)
H1_PAPER_SUMMARY = re.compile(r"(?is)<h1[^>]*>.*?paper\s*summary.*?</h1>")
H2_HEADER = re.compile(r"(?is)<h2[^>]*>(.*?)</h2>")
TAG = re.compile(r"(?is)<[^>]+>")  # generic tag stripper (after targeted replacements)
BR = re.compile(r"(?is)<br\s*/?>")
P_OPEN = re.compile(r"(?is)<p[^>]*>")
P_CLOSE = re.compile(r"(?is)</p>")
NBSP = re.compile(r"&nbsp;")
MULTIBLANK = re.compile(r"\n{3,}")

def html_to_markdown_preserve_meta(html: str) -> str:
    if not html:
        return ""

    # Ensure META comments remain as literal text (we don't remove them)
    # Normalize H1 "Paper Summary" → '# Paper Summary'
    text = H1_PAPER_SUMMARY.sub("\n# Paper Summary\n", html)

    # Convert H2 headers → '## ...'
    def _h2_to_md(m):
        inside = m.group(1)
        # Strip inner tags within the H2
        inside = TAG.sub("", inside).strip()
        return f"\n## {inside}\n"
    text = H2_HEADER.sub(_h2_to_md, text)

    # Paragraph & line breaks
    text = BR.sub("\n", text)
    text = P_OPEN.sub("\n", text)
    text = P_CLOSE.sub("\n", text)

    # Remove all other tags EXCEPT we want to keep HTML comments:
    # Replace comments temporarily with placeholders, strip tags, then restore.
    comments = []
    def _keep_comment(m):
        comments.append(m.group(0))
        return f"__HTML_COMMENT_{len(comments)-1}__"

    text = re.sub(r"<!--.*?-->", _keep_comment, text, flags=re.S)

    # Strip remaining tags
    text = TAG.sub("", text)

    # Restore comments
    for i, c in enumerate(comments):
        text = text.replace(f"__HTML_COMMENT_{i}__", c)

    # Entity cleanup
    text = NBSP.sub(" ", text)

    # Collapse excessive blank lines
    text = MULTIBLANK.sub("\n\n", text)
    text = text.strip()

    # Guarantee leading '# Paper Summary' if META exists
    if "<!--META_START-->" in text and not re.search(r"(?m)^\s*#\s*Paper\s+Summary\s*$", text):
        text = "# Paper Summary\n\n" + text

    return text

# ---- Parsing helpers

RE_NOTE_SPLIT = re.compile(r"(?im)^\s*#\s*Paper\s+Summary\s*$")
META_START = r"<!--META_START-->"
META_END = r"<!--META_END-->"
RE_META_BLOCK = re.compile(rf"{META_START}\s*(?P<block>.*?)\s*{META_END}", re.DOTALL)
RE_KEYVAL = re.compile(r"^\s*([^:]+)\s*:\s*(.*)$")

def extract_meta(md: str) -> Dict[str, str]:
    m = RE_META_BLOCK.search(md)
    if not m:
        return {}
    block = m.group("block")
    out: Dict[str, str] = {}
    for ln in block.splitlines():
        if not ln.strip():
            continue
        km = RE_KEYVAL.match(ln)
        if km:
            key, val = km.group(1).strip(), km.group(2).strip()
            out[key] = val
    return out

def extract_section(md: str, header: str) -> str:
    pattern = re.compile(
        rf"(?im)^\s*##\s*{re.escape(header)}\s*$"
        r"(.*?)"
        r"(?=^\s*##\s+\S|\Z)",
        re.DOTALL
    )
    m = pattern.search(md)
    return m.group(1).strip() if m else ""

def split_notes(combined_md: str) -> List[str]:
    parts = RE_NOTE_SPLIT.split(combined_md)
    out = []
    for chunk in parts[1:]:
        content = "# Paper Summary\n" + chunk
        # Require META to avoid false positives
        if "<!--META_START-->" in content and "<!--META_END-->" in content:
            out.append(content.strip())
    return out

def safe_filename(s: str, limit: int = 80) -> str:
    base = re.sub(r"[^\w\s\-\(\)\[\]\._]+", "", s, flags=re.UNICODE).strip()
    base = re.sub(r"\s+", " ", base)
    if len(base) > limit:
        base = base[:limit].rstrip()
    base = base.replace("/", "-").replace("\\", "-")
    return base or "note"

def feature_flags_from_meta(meta: Dict[str, str]) -> Dict[str, str]:
    out = {}
    for k in ["CL", "CR", "FE", "TI", "EX", "GA"]:
        v = meta.get(k, "").strip()
        out[k] = v if v else "n/a"
    return out

def normalize_yesno(val: str) -> str:
    v = (val or "").strip().lower()
    if v.startswith("y"): return "Yes"
    if v.startswith("n"): return "No"
    if v.startswith("p"): return "Partial"
    return val or "n/a"

def yaml_front_matter(meta: Dict[str, str], domain_link: Optional[str], features_links: List[str], tags: List[str]) -> str:
    y: Dict[str, str] = {}
    safe_keys = [
        "Title","Authors","DOI","Year","Publication Type","Discipline/Domain","Subdomain/Topic",
        "Eligibility","Overall Relevance Score","Operationalization Score","Relevance Score",
        "Contains Definition of Actionability","Contains Systematic Features/Dimensions",
        "Contains Explainability","Contains Interpretability","Contains Framework/Model",
        "Operationalization Present","Primary Methodology","Study Context",
        "Geographic/Institutional Context","Target Users/Stakeholders","Primary Contribution Type",
        "Reason if Not Eligible"
    ]
    for k in safe_keys:
        if k in meta:
            y[k] = str(meta[k])
    if domain_link:
        y["Domain Note"] = domain_link
    if features_links:
        y["Feature Notes"] = features_links
    if tags:
        y["tags"] = tags

    lines = ["---"]
    for k, v in y.items():
        if isinstance(v, list):
            lines.append(f'{k}:')
            for item in v:
                lines.append(f'  - "{item}"')
        else:
            vv = str(v).replace('"','\'')
            lines.append(f'{k}: "{vv}"')
    lines.append("---")
    return "\n".join(lines)

def wrap_wikilink(title: str) -> str:
    return f"[[{title}]]"

def concept_note_title(code: str, label: str = "") -> str:
    mapping = {
        "CL": "Clarity (Actionability)",
        "CR": "Contextual Relevance (Actionability)",
        "FE": "Feasibility (Actionability)",
        "TI": "Timeliness (Actionability)",
        "EX": "Explainability (Actionability)",
        "GA": "Goal Alignment (Actionability)"
    }
    name = mapping.get(code, label or code)
    return f"Concept/{code} - {name}"

def domain_note_title(domain: str) -> str:
    return f"Domain/{domain}"

def build_obsidian_from_combined(
    input_path: Path,
    out_dir: Path,
    title_prefix: str = "",
    min_similarity: float = 0.55,
    max_seealso: int = 5
):
    out_dir.mkdir(parents=True, exist_ok=True)

    # Read content: file OR folder
    if input_path.is_dir():
        parts: List[str] = []
        md_files = sorted(input_path.glob("*.md"))
        html_files = sorted(input_path.glob("*.html"))
        if not md_files and not html_files:
            raise SystemExit(f"No .md or .html files found in folder: {input_path}")

        for f in md_files:
            t = f.read_text(encoding="utf-8")
            # Ensure '# Paper Summary' heading exists if META present
            if "<!--META_START-->" in t and not re.search(r"(?m)^\s*#\s*Paper\s+Summary\s*$", t):
                t = "# Paper Summary\n\n" + t
            parts.append(t)

        for f in html_files:
            html = f.read_text(encoding="utf-8")
            parts.append(html_to_markdown_preserve_meta(html))

        combined_md = "\n\n---\n\n".join(parts)
    else:
        if not input_path.exists():
            raise SystemExit(f"Input not found: {input_path}")
        combined_md = input_path.read_text(encoding="utf-8")

    notes = split_notes(combined_md)
    if not notes:
        raise SystemExit(
            "No notes detected. Ensure each note has a '# Paper Summary' heading AND a <!--META_START--> block.\n"
            "When using HTML input, this script converts <h1>Paper Summary</h1> → '# Paper Summary' and preserves META comments."
        )

    parsed: List[Dict] = []
    for i, raw in enumerate(notes, 1):
        meta = extract_meta(raw)
        title = meta.get("Title", "").strip() or f"Untitled {i}"
        year = meta.get("Year", "").strip()
        domain = meta.get("Discipline/Domain", meta.get("Domain","")).strip()
        subdomain = meta.get("Subdomain/Topic","").strip()

        def sect(name: str) -> str:
            return extract_section(raw, name)

        parsed.append({
            "raw": raw,
            "meta": meta,
            "title": title,
            "year": year,
            "domain": domain,
            "subdomain": subdomain,
            "action_understood": sect("How Actionability is Understood"),
            "general_summary": sect("General Summary of the Paper"),
            "makes_actionable": sect("What Makes Something Actionable"),
            "operationalized": sect("How Actionability is Achieved / Operationalized"),
            "features_block": sect("Dimensions and Attributes of Actionability (Authors’ Perspective)"),
            "foundations": sect("Theoretical or Conceptual Foundations"),
            "indicators": sect("Indicators or Metrics for Actionability"),
            "barriers_enablers": sect("Barriers and Enablers to Actionability"),
            "relation": sect("Relation to Existing Literature"),
            "summary": sect("Summary"),
            "scores": sect("Scores"),
            "quotes": sect("Supporting Quotes from the Paper"),
            "refs": sect("Actionability References to Other Papers"),
            "flags": feature_flags_from_meta(meta)
        })

    # Similarity
    sims: Dict[int, List[Tuple[int, float]]] = defaultdict(list)
    texts = [n["action_understood"] for n in parsed]
    for i in range(len(parsed)):
        for j in range(i+1, len(parsed)):
            s = str_sim(texts[i], texts[j])
            if s >= min_similarity:
                sims[i].append((j, s))
                sims[j].append((i, s))
    for k in sims:
        sims[k].sort(key=lambda t: t[1], reverse=True)

    concept_index: Dict[str, List[str]] = defaultdict(list)
    domain_index: Dict[str, List[str]] = defaultdict(list)

    file_map: Dict[int, str] = {}
    for idx, n in enumerate(parsed):
        title = n["title"]
        year = f" ({n['year']})" if n["year"] else ""
        file_title = f"{title_prefix+' ' if title_prefix else ''}{title}{year}".strip()
        fname = safe_filename(file_title) + ".md"
        file_path = out_dir / fname

        domain_title = domain_note_title(n["domain"]) if n["domain"] else None
        domain_link = wrap_wikilink(domain_title) if n["domain"] else None
        if n["domain"]:
            domain_index[n["domain"]].append(wrap_wikilink(file_title))

        feature_links: List[str] = []
        tags: List[str] = []
        for code, val in n["flags"].items():
            norm = normalize_yesno(val)
            if norm.lower().startswith(("yes", "partial")):
                ctitle = concept_note_title(code)
                link = wrap_wikilink(ctitle)
                feature_links.append(link)
                concept_index[code].append(wrap_wikilink(file_title))
                tags.append(f"feature/{code.lower()}")

        yaml = yaml_front_matter(n["meta"], domain_link, feature_links, tags)

        see_also_lines = []
        neighbors = sims.get(idx, [])[:max_seealso]
        if neighbors:
            see_also_lines.append("## See also")
            for j, score in neighbors:
                other = parsed[j]
                oth_title = f"{title_prefix+' ' if title_prefix else ''}{other['title']}{' ('+other['year']+')' if other['year'] else ''}"
                see_also_lines.append(f"- {wrap_wikilink(oth_title)}  ^sim{int(score*100)}")

        body_lines = [
            yaml,
            f"# {title}{year}",
        ]
        authors = n["meta"].get("Authors","").strip()
        if authors:
            body_lines.append(f"*{authors}*")
        if n["meta"].get("DOI"):
            body_lines.append(f"**DOI:** {n['meta']['DOI']}")
        if n["domain"]:
            body_lines.append(f"**Domain:** {domain_link if domain_link else n['domain']}")
        if n["subdomain"]:
            body_lines.append(f"**Subdomain/Topic:** {n['subdomain']}")
        body_lines.append("")

        if n["general_summary"]:
            body_lines += ["## General Summary of the Paper", n["general_summary"], ""]
        if n["action_understood"]:
            body_lines += ["## How Actionability is Understood", n["action_understood"], ""]
        if n["makes_actionable"]:
            body_lines += ["## What Makes Something Actionable", n["makes_actionable"], ""]
        if n["operationalized"]:
            body_lines += ["## How Actionability is Achieved / Operationalized", n["operationalized"], ""]
        if n["features_block"]:
            body_lines += ["## Dimensions and Attributes of Actionability (Authors’ Perspective)", n["features_block"], ""]
        if n["foundations"]:
            body_lines += ["## Theoretical or Conceptual Foundations", n["foundations"], ""]
        if n["indicators"]:
            body_lines += ["## Indicators or Metrics for Actionability", n["indicators"], ""]
        if n["barriers_enablers"]:
            body_lines += ["## Barriers and Enablers to Actionability", n["barriers_enablers"], ""]
        if n["relation"]:
            body_lines += ["## Relation to Existing Literature", n["relation"], ""]
        if n["summary"]:
            body_lines += ["## Actionability-Focused Summary", n["summary"], ""]
        if n["quotes"]:
            body_lines += ["## Supporting Quotes from the Paper", n["quotes"], ""]
        if n["refs"]:
            body_lines += ["## Actionability References to Other Papers", n["refs"], ""]
        if see_also_lines:
            body_lines += see_also_lines + [""]

        file_path.write_text("\n".join(body_lines).strip() + "\n", encoding="utf-8")
        file_map[idx] = file_title

    # Concept pages
    concept_dir = out_dir / "Concept"
    concept_dir.mkdir(parents=True, exist_ok=True)
    concept_names = {
        "CL": "Clarity (Actionability)",
        "CR": "Contextual Relevance (Actionability)",
        "FE": "Feasibility (Actionability)",
        "TI": "Timeliness (Actionability)",
        "EX": "Explainability (Actionability)",
        "GA": "Goal Alignment (Actionability)"
    }
    for code, pages in concept_index.items():
        path = concept_dir / f"{code} - {concept_names.get(code, code)}.md"
        lines = [
            f"# {code} — {concept_names.get(code, code)}",
            "",
            "> Papers that explicitly treat this dimension as **important for actionability**:",
            ""
        ]
        for p in sorted(set(pages)):
            lines.append(f"- {p}")
        path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    # Domain pages
    domain_dir = out_dir / "Domain"
    domain_dir.mkdir(parents=True, exist_ok=True)
    for d, pages in domain_index.items():
        path = domain_dir / f"{safe_filename(d)}.md"
        lines = [f"# {d}", "", "## Papers", ""]
        for p in sorted(set(pages)):
            lines.append(f"- {p}")
        path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    # Global index
    index_path = out_dir / "Actionability Index.md"
    lines = ["# Actionability Index", ""]
    lines.append("## By Domain")
    for d in sorted(domain_index.keys(), key=lambda s: s.lower()):
        lines.append(f"- {wrap_wikilink(domain_note_title(d))}")
    lines += ["", "## By Concept"]
    for code in ["CL","CR","FE","TI","EX","GA"]:
        lines.append(f"- {wrap_wikilink(concept_note_title(code))}")
    lines += ["", "## All Papers"]
    for idx in range(len(parsed)):
        lines.append(f"- {wrap_wikilink(file_map[idx])}")
    index_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    print(f"Built {len(parsed)} paper notes into: {out_dir}")
    print("Created concept and domain pages, and 'Actionability Index.md'.")

# ---- CLI
def main():
    ap = argparse.ArgumentParser(description="Build Obsidian notes from Actionability notes (.md or .html).")
    ap.add_argument("--input", required=True, help="Path to combined notes .md OR folder containing per-note .md/.html")
    ap.add_argument("--outdir", required=True, help="Output folder for Obsidian-ready notes")
    ap.add_argument("--title-prefix", default="", help="Optional prefix for each paper title in filenames")
    ap.add_argument("--min-similarity", type=float, default=0.55, help="Min similarity (0-1) for 'See also' linking")
    ap.add_argument("--max-seealso", type=int, default=5, help="Max 'See also' links per paper")
    args = ap.parse_args()

    input_path = Path(args.input)
    out_dir = Path(args.outdir)
    build_obsidian_from_combined(
        input_path=input_path,
        out_dir=out_dir,
        title_prefix=args.title_prefix,
        min_similarity=args.min_similarity,
        max_seealso=args.max_seealso
    )

if __name__ == "__main__":
    main()
