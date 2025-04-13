import os
import json
from src.mappings.optional_fields_map import optional_fields_map

def get_tag_path(tag_name):
    return os.path.join("resources/data/minecraft/tags", tag_name + ".json")

def load_tag(tag_path):
    try:
        with open(tag_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"replace": False, "values": []}

def save_tag(tag_path, tag_data):
    with open(tag_path, "w") as f:
        json.dump(tag_data, f, indent=2)

def append_to_tag(tag_name, value):
    tag_path = get_tag_path(tag_name)
    tag_data = load_tag(tag_path)

    if value not in tag_data["values"]:
        tag_data["values"].append(value)
        print(f"Appended to tag: {tag_path} -> {value}")

    save_tag(tag_path, tag_data)

def remove_from_tag(tag_name, value):
    tag_path = get_tag_path(tag_name)
    tag_data = load_tag(tag_path)

    if value in tag_data["values"]:
        tag_data["values"].remove(value)
        print(f"Removed from tag: {tag_path} -> {value}")

    save_tag(tag_path, tag_data)

def handle_optional_tags(item_type, item_id, mod_name, **kwargs):
    block_id = f"{mod_name}:{item_id}"
    field_map = optional_fields_map.get(item_type, {})

    for field_name, value_map in field_map.items():
        user_value = kwargs.get(field_name, None)

        for option_value, tag_name in value_map.items():
            if user_value == option_value:
                append_to_tag(tag_name, block_id)
            else:
                remove_from_tag(tag_name, block_id)
