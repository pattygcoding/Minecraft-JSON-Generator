from src.tags.lang import update_lang_file
from src.processes.processes import handle_type_case

def process_entries(inputs, template_map, mod_name):
    if not isinstance(inputs, list):
        raise ValueError("input.json should be a list of objects")

    lang_entries = {}

    for input_obj in inputs:
        item_type = input_obj.get("type")
        item_id = input_obj.get("id")
        item_name = input_obj.get("name", "")

        if not item_type or not item_id:
            print(f"Skipping entry (missing type or id): {input_obj}")
            continue

        type_info = template_map.get(item_type)
        if not type_info:
            print(f"Unsupported type: {item_type} (skipping)")
            continue

        if not handle_type_case(item_type, type_info, mod_name, **input_obj):
            print(f"Warning: No case handler for type: {item_type} (skipping {item_id})")
            continue

        # Add language key
        category = item_type.split("/")[0]
        lang_key = f"{category}.{mod_name}.{item_id}"
        lang_entries[lang_key] = item_name

    update_lang_file(mod_name, lang_entries)
