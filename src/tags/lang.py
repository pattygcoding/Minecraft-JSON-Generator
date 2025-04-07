import os
import json

def update_lang_file(mod_name, new_entries):
    lang_path = os.path.join("resources/assets", mod_name, "lang", "en_us.json")
    os.makedirs(os.path.dirname(lang_path), exist_ok=True)

    try:
        with open(lang_path, "r") as f:
            existing_lang = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_lang = {}

    existing_lang.update(new_entries)

    with open(lang_path, "w") as f:
        json.dump(existing_lang, f, indent=4, ensure_ascii=False)

    print(f"Updated language file: {lang_path}")
