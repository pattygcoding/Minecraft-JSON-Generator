import os
import json
from src.mappings.required_fields_map import required_fields_map

def handle_type_case(item_type, type_info, mod_name, **kwargs):
    item_id = kwargs.get("id")

    required_fields = required_fields_map.get(item_type, [])
    missing = [field for field in required_fields if not kwargs.get(field)]
    if missing:
        print(f"Error: missing required field(s) {missing} for type '{item_type}' (skipping {item_id or 'unknown'})")
        return False

    for tmpl in type_info.get("templates", []):
        if "tag_append" in tmpl:
            tag_path = tmpl["tag_append"]
            value_template = tmpl.get("value_format", "{id}")
            value = value_template.format(**kwargs, mod_name=mod_name)

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
        output_path = os.path.join(output_dir, f"{item_id}.json")

        try:
            with open(template_path, "r") as f:
                template = f.read()

            rendered = template
            for key, value in kwargs.items():
                rendered = rendered.replace(f"{{{{{key}}}}}", str(value))
            rendered = rendered.replace("{mod_name}", mod_name).replace("{id}", item_id)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w") as f:
                f.write(rendered)

            print(f"Generated {output_path}")
        except Exception as e:
            print(f"Error processing template {template_path} for {item_id}: {e}")

    return True
