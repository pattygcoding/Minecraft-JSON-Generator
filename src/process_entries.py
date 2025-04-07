import os
from src.tags.lang import update_lang_file

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

        for tmpl in type_info.get("templates", []):
            template_path = tmpl["source"]
            output_template = tmpl["output"]

            # Inject mod_name into output path
            output_dir = output_template.replace("{mod_name}", mod_name)
            output_path = os.path.join(output_dir, f"{item_id}.json")

            try:
                with open(template_path, "r") as f:
                    template = f.read()

                rendered = template.replace("{mod_name}", mod_name).replace("{id}", item_id)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                with open(output_path, "w") as f:
                    f.write(rendered)

                print(f"Generated {output_path}")
            except Exception as e:
                print(f"Error processing template {template_path} for {item_id}: {e}")

        # Generate lang entry
        category = item_type.split("/")[0]
        lang_key = f"{category}.{mod_name}.{item_id}"
        lang_entries[lang_key] = item_name

    update_lang_file(mod_name, lang_entries)
