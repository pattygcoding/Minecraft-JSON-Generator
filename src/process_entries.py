import os
from mappings.lib import getJsonMap
from src.helpers.extract_json_values import extract_json_values
from src.processes.processes import handle_type_case
from src.tags.lang.lang import update_lang_file
from src.tags.tools.tool_material_tags import update_tool_material_tags

def process_entries(inputs, template_map, mod_name):
    if not isinstance(inputs, list):
        raise ValueError("input.json should be a list of objects")

    lang_entries = {}
    default_advancements = getJsonMap("advancements", "default")
    tool_types = {"item/axe", "item/pickaxe", "item/sword", "item/hoe", "item/shovel"}

    for input_obj in inputs:
        item_type = input_obj.get("type")
        base_id = input_obj.get("id")
        base_name = input_obj.get("name", "")
        material = input_obj.get("material", base_id)

        if not item_type or not base_id:
            print(f"Skipping entry (missing type or id): {input_obj}")
            continue

        # Handle sets like "set/armor", "set/tools"
        if item_type.startswith("set/"):
            set_templates = template_map.get(item_type)
            if not set_templates:
                print(f"Unsupported set type: {item_type} (skipping)")
                continue

            json_values = extract_json_values(set_templates["templates"], default_advancements)

            for suffix in json_values:
                type_key = f"item/{suffix}"
                type_info = template_map.get(type_key)

                if not type_info:
                    print(f"Missing type info for {type_key} (skipping)")
                    continue

                full_id = f"{base_id}_{suffix}"
                full_name = f"{base_name} {suffix.replace('_', ' ').title()}"

                success = handle_type_case(type_key, type_info, mod_name,
                    id=full_id,
                    name=full_name,
                    material=material
                )

                if success:
                    lang_entries[f"item.{mod_name}.{full_id}"] = full_name

                    if type_key in tool_types:
                        update_tool_material_tags(mod_name, material)
                else:
                    print(f"Failed to process: {full_id} ({type_key})")

            continue

        # Handle regular item types
        type_info = template_map.get(item_type)
        if not type_info:
            print(f"Unsupported type: {item_type} (skipping)")
            continue

        if handle_type_case(item_type, type_info, mod_name, **input_obj):
            category = item_type.split("/")[0]
            lang_entries[f"{category}.{mod_name}.{base_id}"] = base_name

            if item_type in tool_types:
                update_tool_material_tags(mod_name, material)
        else:
            print(f"Failed to process: {base_id} ({item_type})")

    update_lang_file(mod_name, lang_entries)
