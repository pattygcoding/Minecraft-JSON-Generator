import os
from src.tags.lang import update_lang_file
from src.processes.processes import handle_type_case
from src.mappings.advancement_default_map import SUFFIX_MAP

def process_entries(inputs, template_map, mod_name):
    if not isinstance(inputs, list):
        raise ValueError("input.json should be a list of objects")

    lang_entries = {}

    for input_obj in inputs:
        item_type = input_obj.get("type")
        base_id = input_obj.get("id")
        base_name = input_obj.get("name", "")
        material = input_obj.get("material", base_id)

        if not item_type or not base_id:
            print(f"Skipping entry (missing type or id): {input_obj}")
            continue

        # Handle sets like "set/armor"
        if item_type.startswith("set/"):
            set_templates = template_map.get(item_type)
            if not set_templates:
                print(f"Unsupported set type: {item_type} (skipping)")
                continue

            # Extract unique recipe suffixes from recipe sources only
            recipe_suffixes = set()
            for t in set_templates["templates"]:
                source_path = t.get("source", "")
                if "/recipes/" in source_path and source_path.endswith(".json"):
                    suffix = os.path.splitext(os.path.basename(source_path))[0]

                    # Remap 'default' filenames to real suffixes based on folder path
                    if suffix == "default":
                        for folder, mapping in SUFFIX_MAP.items():
                            if f"/{folder}/" in source_path:
                                if isinstance(mapping, dict):
                                    for keyword, resolved in mapping.items():
                                        if keyword != "default" and keyword in source_path:
                                            suffix = resolved
                                            break
                                    else:
                                        suffix = mapping.get("default", "item")
                                else:
                                    suffix = mapping
                                break
                        else:
                            suffix = SUFFIX_MAP.get("default", "item")  # final fallback

                    recipe_suffixes.add(suffix)

            for suffix in recipe_suffixes:
                type_key = f"item/{suffix}"
                type_info = template_map.get(type_key)

                if not type_info:
                    print(f"Missing type info for {type_key} (skipping)")
                    continue

                full_id = f"{base_id}_{suffix}"  # e.g. ruby_helmet
                full_name = f"{base_name} {suffix.replace('_', ' ').title()}"  # Ruby Helmet

                success = handle_type_case(type_key, type_info, mod_name,
                    id=full_id,
                    name=full_name,
                    material=material
                )

                if success:
                    lang_entries[f"item.{mod_name}.{full_id}"] = full_name
                else:
                    print(f"Failed to process: {full_id} ({type_key})")

            continue  # done with set

        # Handle normal individual items
        type_info = template_map.get(item_type)
        if not type_info:
            print(f"Unsupported type: {item_type} (skipping)")
            continue

        if handle_type_case(item_type, type_info, mod_name, **input_obj):
            category = item_type.split("/")[0]
            lang_entries[f"{category}.{mod_name}.{base_id}"] = base_name
        else:
            print(f"Failed to process: {base_id} ({item_type})")

    update_lang_file(mod_name, lang_entries)
