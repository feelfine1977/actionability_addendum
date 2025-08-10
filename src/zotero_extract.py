# pip install pyzotero
from pyzotero import zotero
from datetime import datetime
import time
import os
import html

# ---- CONFIG ----
LIBRARY_ID   = "2095933"   # e.g., "1234567"
LIBRARY_TYPE = "user"                     # "user" or "group"
API_KEY      = "0jOjjqhaPDNWelxXtuieZ3wP"

COLLECTION_NAME = "Actionability_Screening"
REQUIRED_TAGS_ALL = {"Paper_Actionability"}  # must have ALL of these

ADD_RESULT_NOTE_TO_SAME_COLLECTION = True
RESULT_NOTE_TAGS = ["Merged_Notes", COLLECTION_NAME]

OUTPUT_FILENAME = f"merged_notes_{COLLECTION_NAME}.html"
THROTTLE_SECONDS = 0.1  # gentle pacing for API (tweak if you hit rate limits)

# ========================
# CONNECT
# ========================
zot = zotero.Zotero(LIBRARY_ID, LIBRARY_TYPE, API_KEY)

# ========================
# HELPERS
# ========================
def pause():
    if THROTTLE_SECONDS:
        time.sleep(THROTTLE_SECONDS)

def find_collection_by_name(name: str):
    """
    Return the first collection whose name exactly matches `name`.
    """
    # everything() auto-paginates
    cols = zot.everything(zot.collections())
    pause()
    for c in cols:
        if c["data"]["name"] == name:
            return c
    return None

def get_top_level_items_for_collection(coll_key: str):
    """
    Get ALL top-level items (no notes/attachments) for the collection.
    """
    items = zot.everything(zot.collection_items_top(coll_key))
    pause()
    return items

def item_tags_set(item) -> set:
    return {t.get("tag", "") for t in item["data"].get("tags", []) if "tag" in t}

def has_all_required_tags(item, required: set) -> bool:
    tags = item_tags_set(item)
    return required.issubset(tags)

def get_child_notes_html(parent_key: str):
    """
    Returns a list of HTML strings — the note bodies for a given parent.
    """
    notes = []
    children = zot.everything(zot.children(parent_key))
    pause()
    for ch in children:
        if ch["data"].get("itemType") == "note":
            notes.append(ch["data"].get("note", ""))  # already HTML
    return notes

# ========================
# MAIN
# ========================
# 1) find collection
collection = find_collection_by_name(COLLECTION_NAME)
if not collection:
    raise SystemExit(f"Collection '{COLLECTION_NAME}' not found.")
coll_key = collection["data"]["key"]

# 2) fetch top-level items
items = get_top_level_items_for_collection(coll_key)

# 3) filter to items that have ALL required tags
filtered = [it for it in items if has_all_required_tags(it, REQUIRED_TAGS_ALL)]

# 4) collect notes per item and assemble sections
sections = []
for it in filtered:
    title = it["data"].get("title") or "(untitled)"
    safe_title = html.escape(title)
    key = it["key"]

    notes_html = get_child_notes_html(key)
    if not notes_html:
        continue

    section = []
    section.append(f'<h2>{safe_title}</h2>')
    section.append(f'<p><em>Key: {key}</em></p>')
    for n in notes_html:
        # each note is valid HTML; wrap for separation
        section.append(f'<div class="zotero-note">{n}</div>')
    section.append("<hr/>")
    sections.append("\n".join(section))

if not sections:
    raise SystemExit(
        f"No child notes found for items in '{COLLECTION_NAME}' "
        f"that have ALL tags: {sorted(REQUIRED_TAGS_ALL)}"
    )

# 5) build final HTML (avoid f-string backslash issue by pre-joining)
merged_html_content = "\n".join(sections)
generated_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

final_html = (
    "<!DOCTYPE html>\n"
    "<html>\n<head>\n<meta charset=\"utf-8\"/>\n"
    f"<title>Merged Notes - {COLLECTION_NAME}</title>\n"
    "</head>\n<body>\n"
    f"<h1>Merged Notes — {COLLECTION_NAME}</h1>\n"
    f"<p><em>Generated: {generated_str}</em></p>\n"
    f"{merged_html_content}\n"
    "</body>\n</html>\n"
)

# 6) save locally
with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Saved {OUTPUT_FILENAME} to {os.path.abspath(OUTPUT_FILENAME)}")

# 7) optionally create a single merged note back in Zotero
if ADD_RESULT_NOTE_TO_SAME_COLLECTION:
    new_note = {
        "itemType": "note",
        "note": final_html,  # Zotero notes accept HTML
        "tags": [{"tag": t} for t in RESULT_NOTE_TAGS],
        "collections": [coll_key],
    }
    created = zot.create_items([new_note])
    print("Created Zotero note:", created)