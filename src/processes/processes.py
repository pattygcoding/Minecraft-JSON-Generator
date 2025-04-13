import os
import json
from mappings.lib import getJsonMap
from src.processes.optional.optional_handling import handle_optional_tags
    
def handle_type_case(item_type, type_info, mod_name, **kwargs):
    item_id = kwargs.get("id")

    required_fields = getJsonMap("fields", "required").get(item_type, [])

    missing = [field for field in required_fields if field not in kwargs]
    if missing:
        print(f"Error: missing required field(s) {missing} for type '{item_type}' (skipping {item_id or 'unknown'})")
        return False

    is_vanilla = item_type.endswith("/vanilla")
    mod_name_v = "minecraft" if is_vanilla else mod_name

    for tmpl in type_info.get("templates", []):
        if not isinstance(tmpl, dict):
            print(f"Skipping malformed template: {tmpl} (not a dict)")
            continue
    
        if "tag_append" in tmpl:
            tag_path = tmpl["tag_append"]

            default_format = " - ".join(f"{{{field}}}" for field in required_fields)
            value_template = tmpl.get("value_format", default_format)

            replacements = {
                **kwargs,
                "mod_name": mod_name,
                "mod_name_v": mod_name_v,
                "id": item_id
            }

            value = value_template.format(**replacements)

            abs_path = os.path.join(tag_path)
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)

            try:
                with open(abs_path, "r") as f:
                    tag_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                tag_data = {"replace": False, "values": []}

            if value not in tag_data["values"]:
                tag_data["values"].append(value)

            with open(abs_path, "w") as f:
                json.dump(tag_data, f, indent=2)

            print(f"Appended to tag: {abs_path} -> {value}")
            continue

        # Handle normal template rendering
        template_path = tmpl["source"]
        output_dir = tmpl["output"].replace("{mod_name}", mod_name)
        
        # support custom output file naming if dynamic_filename is present
        if "dynamic_filename" in tmpl:
            dyn_name = tmpl["dynamic_filename"]

            if "full_block" in kwargs and "{full_block}" in dyn_name:
                filename = dyn_name.format(**kwargs)
            elif "full_block" in kwargs and dyn_name == "slab_from_full_block_stonecutting":
                filename = f"{item_id}_from_{kwargs['full_block']}_stonecutting"
            else:
                if dyn_name in getJsonMap("types", "stonecutting"):
                    filename = item_id  # clean default name
                else:
                    filename = f"{item_id}_{dyn_name}"

            output_path = os.path.join(output_dir, f"{filename}.json")
        else:
            output_path = os.path.join(output_dir, f"{item_id}.json")


        try:
            with open(template_path, "r") as f:
                template = f.read()

            replacements = {
                **kwargs,
                "mod_name": mod_name,
                "mod_name_v": mod_name_v,
                "id": item_id
            }

            for key, value in replacements.items():
                template = template.replace(f"{{{key}}}", str(value))

            rendered = template

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as f:
                f.write(rendered)

            print(f"Generated {output_path}")
        except Exception as e:
            print(f"Error processing template {template_path} for {item_id}: {e}")

    handle_optional_tags(item_type, item_id, mod_name, **kwargs)

    return True