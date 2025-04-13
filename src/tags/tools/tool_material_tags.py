import os
import json

def update_tool_material_tags(mod_name, material):
    tag_path = os.path.join(
        "resources", "data", mod_name, "tags", "items", f"{material}_tool_materials.json"
    )
    os.makedirs(os.path.dirname(tag_path), exist_ok=True)

    try:
        with open(tag_path, "r") as f:
            tag_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tag_data = {"replace": False, "values": []}

    identifier = f"{mod_name}:{material}"
    if identifier not in tag_data["values"]:
        tag_data["values"].append(identifier)

        with open(tag_path, "w") as f:
            json.dump(tag_data, f, indent=2)

        print(f"Created/updated tag: {tag_path} with value {identifier}")
