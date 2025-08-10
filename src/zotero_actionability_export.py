#!/usr/bin/env python3
"""
Zotero Actionability Export – Expanded Note Parser (Locked Header + Dual Scoring + Raw Markdown)

Features:
- Reads notes in the new expanded Markdown format
- Extracts all fields from <!--META_START--> block + all body sections
- Synonym mapping (e.g., Discipline/Domain → Domain)
- Fills missing fields with "n/a" (numeric scores default to 0)
- Locked column order for consistent comparative analysis
- Adds a "Raw Markdown" column for reference
- Supports tag filtering by note, parent, or either
- Supports accept_any_note mode
- Safe child-note fetching (avoids API 400 errors for attachments)
- Produces:
    - Excel with locked column order
    - Combined PDF/HTML of all notes
    - Per-note PDF/HTML
 python zotero_actionability_export.py --config zotero_export_config.yml  
"""

import os
import re
import json
import argparse
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import pandas as pd

# Lazy imports
def lazy_imports():
    global Zotero, BeautifulSoup, markdown2
    from pyzotero import zotero as _z
    Zotero = _z.Zotero
    from bs4 import BeautifulSoup as _bs
    BeautifulSoup = _bs
    import markdown2 as _md2
    markdown2 = _md2

# Config loader
def load_config(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"Config file not found: {path}")
    if path.suffix.lower() in {".yml", ".yaml"}:
        try:
            import yaml
        except ImportError:
            raise SystemExit("PyYAML is required for YAML configs. Install with: pip install pyyaml")
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# Locked header order
LOCKED_COLUMNS = [
    # META fields
    "Title", "Authors", "DOI", "Year", "Publication Type", "Discipline/Domain", "Subdomain/Topic",
    "Domain", "Eligibility", "Overall Relevance Score", "Operationalization Score", "Relevance Score",
    "Contains Definition of Actionability", "Contains Systematic Features/Dimensions",
    "Contains Explainability", "Contains Interpretability", "Contains Framework/Model",
    "Operationalization Present", "Primary Methodology", "Study Context", "Geographic/Institutional Context",
    "Target Users/Stakeholders", "Primary Contribution Type",
    "CL", "CR", "FE", "TI", "EX", "GA", "Reason if Not Eligible",
    # Body sections
    "Contextual Background", "How Actionability is Understood", "What Makes Something Actionable",
    "How Actionability is Achieved / Operationalized",
    "Systematic Features or Dimensions the Authors Claim are Important for Actionability",
    "Theoretical or Conceptual Foundations", "Indicators or Metrics for Actionability",
    "Barriers and Enablers to Actionability", "Relation to Existing Literature",
    "Summary", "Supporting Quotes from the Paper", "Actionability References to Other Papers",
    # Raw markdown column
    "Raw Markdown"
]

META_START = r"<!--META_START-->"
META_END = r"<!--META_END-->"
RE_META_BLOCK = re.compile(rf"{META_START}\s*(?P<block>.*?)\s*{META_END}", re.DOTALL)
RE_KEYVAL = re.compile(r"^\s*([^:]+)\s*:\s*(.*)$")
RE_PS_HEADER = re.compile(r"^\s*#\s*Paper\s+Summary\b", re.IGNORECASE | re.MULTILINE)

# HTML to Markdown
def html_to_markdown_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for br in soup.find_all(["br"]):
        br.replace_with("\n")
    for p in soup.find_all("p"):
        if p.text and not p.text.endswith("\n"):
            p.append("\n")
    return soup.get_text().strip()

# Parse META block
def parse_meta_block(md_text: str) -> Dict[str, str]:
    out = {}
    m = RE_META_BLOCK.search(md_text)
    if not m:
        return out
    block = m.group("block")
    for ln in block.splitlines():
        if not ln.strip():
            continue
        km = RE_KEYVAL.match(ln)
        if km:
            key = km.group(1).strip()
            val = km.group(2).strip()
            out[key] = val
    return out

# Parse body sections
def parse_section(md_text: str, header: str) -> str:
    pattern = re.compile(
        rf"(?mi)^##\s*{re.escape(header)}\s*$"
        r"(.*?)"
        r"(?=^\s*##\s+\S|\Z)",
        re.DOTALL
    )
    m = pattern.search(md_text)
    return m.group(1).strip() if m else "n/a"

# Parse note
def parse_note_markdown(md_text: str, accept_any_note: bool=False) -> Optional[Dict[str, str]]:
    if not md_text:
        return None
    if not accept_any_note and not RE_PS_HEADER.search(md_text):
        return None

    meta = parse_meta_block(md_text)
    if not meta.get("Title", "").strip():
        return None

    row = {}
    for col in LOCKED_COLUMNS:
        if col == "Raw Markdown":
            row[col] = md_text
        elif col in meta:
            val = meta[col]
            if col in ["Overall Relevance Score", "Operationalization Score", "Relevance Score"]:
                try:
                    row[col] = float(val)
                except:
                    row[col] = 0
            else:
                row[col] = val if val else "n/a"
        else:
            # Synonym mapping
            if col == "Domain" and "Discipline/Domain" in meta:
                row[col] = meta["Discipline/Domain"]
            elif col in [
                "Contextual Background", "How Actionability is Understood",
                "What Makes Something Actionable", "How Actionability is Achieved / Operationalized",
                "Systematic Features or Dimensions the Authors Claim are Important for Actionability",
                "Theoretical or Conceptual Foundations", "Indicators or Metrics for Actionability",
                "Barriers and Enablers to Actionability", "Relation to Existing Literature",
                "Summary", "Supporting Quotes from the Paper", "Actionability References to Other Papers"
            ]:
                row[col] = parse_section(md_text, col)
            else:
                row[col] = "n/a"
    return row

# Zotero helpers
def pick_collection(zot, name: str) -> Optional[Dict[str, Any]]:
    cols = zot.collections()
    for c in cols:
        if c["data"]["name"] == name:
            return c
    for c in cols:
        if c["data"]["name"].lower() == name.lower():
            return c
    return None

def item_tags(item: Optional[Dict[str, Any]]) -> List[str]:
    if not item:
        return []
    return [t.get("tag", "") for t in item.get("data", {}).get("tags", [])]

def tags_match(candidate_tags: List[str], selected: List[str], mode: str) -> bool:
    if not selected:
        return True
    cset = set(map(str.lower, candidate_tags))
    sset = set(map(str.lower, selected))
    return sset.issubset(cset) if mode == "all" else bool(cset & sset)

# Load notes safely
def load_collection_notes(zot, collection_key: str, selected_tags: List[str],
                           tag_mode: str, tag_scope: str, accept_any_note: bool) -> List[Dict[str, Any]]:
    results = []

    # Standalone notes
    standalone = zot.everything(zot.collection_items(collection_key, itemType="note"))
    for it in standalone:
        cand_tags = item_tags(it)
        if not tags_match(cand_tags, selected_tags, tag_mode):
            continue
        md_text = html_to_markdown_text(it["data"].get("note", "") or "")
        parsed = parse_note_markdown(md_text, accept_any_note=accept_any_note)
        if parsed:
            results.append({"key": it["key"], "markdown": md_text, "parsed": parsed})

    # Child notes of valid top-level items
    top_level = zot.everything(zot.collection_items(collection_key))
    for parent in top_level:
        item_type = parent["data"].get("itemType", "")
        if item_type == "note" or parent["data"].get("parentItem"):
            continue
        if item_type.lower() in {"attachment", "pdf", "epub", "snapshot"}:
            continue

        parent_tags = item_tags(parent)
        try:
            children = zot.everything(zot.children(parent["key"]))
        except Exception:
            continue

        for ch in children:
            if ch["data"].get("itemType") != "note":
                continue
            if tag_scope == "note":
                cand_tags = item_tags(ch)
            elif tag_scope == "parent":
                cand_tags = parent_tags
            else:
                cand_tags = list(set(item_tags(ch)) | set(parent_tags))
            if not tags_match(cand_tags, selected_tags, tag_mode):
                continue
            md_text = html_to_markdown_text(ch["data"].get("note", "") or "")
            parsed = parse_note_markdown(md_text, accept_any_note=accept_any_note)
            if parsed:
                results.append({"key": ch["key"], "markdown": md_text, "parsed": parsed})

    return results

# Export helpers
def render_combined_markdown(notes: List[Dict[str, Any]]) -> str:
    return "\n\n".join([n["markdown"].strip() for n in notes])

def _html_from_markdown(md_text: str) -> str:
    return markdown2.markdown(md_text, extras=["fenced-code-blocks","tables","strike","footnotes"])

def combined_markdown_to_pdf(md_text: str, out_pdf_path: Path, out_html_path: Path) -> Tuple[bool, str]:
    html = _html_from_markdown(md_text)
    out_html_path.write_text(html, encoding="utf-8")
    try:
        from weasyprint import HTML as _HTML
        _HTML(string=html).write_pdf(str(out_pdf_path))
        return True, "PDF written with WeasyPrint"
    except Exception:
        try:
            from reportlab.pdfgen import canvas as _canvas
            c = _canvas.Canvas(str(out_pdf_path))
            y = 800
            for line in md_text.splitlines():
                if y < 40:
                    c.showPage()
                    y = 800
                c.drawString(40, y, line[:1100])
                y -= 12
            c.save()
            return True, "PDF written with ReportLab (plain text fallback)"
        except Exception as e2:
            return False, f"PDF failed: {e2}"

def export_per_note(notes: List[Dict[str, Any]], out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    for n in notes:
        slug = re.sub(r"[^A-Za-z0-9._-]+", "_", n["parsed"]["Title"])[:50]
        md = n["markdown"]
        pdf_path = out_dir / f"{slug}.pdf"
        html_path = out_dir / f"{slug}.html"
        combined_markdown_to_pdf(md, pdf_path, html_path)

# Main
def main():
    lazy_imports()
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    cfg = load_config(Path(args.config))
    zot = Zotero(cfg["library_id"], cfg.get("library_type", "user"), cfg["api_key"])
    coll = pick_collection(zot, cfg["collection"])
    if not coll:
        raise SystemExit(f"Collection not found: {cfg['collection']}")

    notes = load_collection_notes(
        zot,
        coll["data"]["key"],
        cfg.get("tags", []),
        cfg.get("tag_mode", "all"),
        cfg.get("tag_scope", "either"),
        cfg.get("accept_any_note", False)
    )

    if not notes:
        print("No matching notes found.")
        return

    df = pd.DataFrame([{col: n["parsed"].get(col, "n/a") for col in LOCKED_COLUMNS} for n in notes])
    out_prefix = Path(cfg.get("out_prefix", "zotero_actionability_export"))
    out_xlsx = out_prefix.with_suffix(".xlsx")
    df.to_excel(out_xlsx, index=False)

    combined_md = render_combined_markdown(notes)
    combined_markdown_to_pdf(combined_md, out_prefix.with_suffix(".pdf"), out_prefix.with_suffix(".html"))

    if cfg.get("per_note_pdf", False):
        export_per_note(notes, Path(cfg.get("per_note_dir", f"{out_prefix}_notes")))

    print(f"Export complete: {out_xlsx}")

if __name__ == "__main__":
    main()
