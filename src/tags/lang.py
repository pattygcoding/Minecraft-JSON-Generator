import os
import json

def update_lang_file(mod_name, new_entries=None, base_name=None, template_set=None):
    lang_path = os.path.join("resources/assets", mod_name, "lang", "en_us.json")
    os.makedirs(os.path.dirname(lang_path), exist_ok=True)

    try:
        with open(lang_path, "r") as f:
            existing_lang = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_lang = {}

    if new_entries is None:
        new_entries = {}

    if base_name and template_set:
        for tmpl in template_set["templates"]:
            source = tmpl.get("source", "")
            if source.endswith(".json"):
                filename = os.path.basename(source).removesuffix(".json")
                entry_key = f"item.{mod_name}.{filename}"
                display_name = f"{base_name} " + filename.replace("_", " ").title()
                new_entries[entry_key] = display_name

    existing_lang.update(new_entries)

    with open(lang_path, "w", encoding="utf-8") as f:
        json.dump(existing_lang, f, indent=4, ensure_ascii=False)

    print(f"Updated language file: {lang_path}")
