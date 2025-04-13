import os
import json
from src.mappings.tag_map import get_tag_keys

def sort_tag_files(mod_name):
    resources_dir = "resources"
    files_to_sort = get_tag_keys(mod_name)

    for rel_path in files_to_sort:
        full_path = os.path.join(resources_dir, rel_path)

        if not os.path.exists(full_path):
            print(f"Skipping missing file: {full_path}")
            continue

        try:
            with open(full_path, "r") as f:
                data = json.load(f)

            sorted_data = dict(sorted(data.items())) 

            with open(full_path, "w") as f:
                json.dump(sorted_data, f, indent=4, ensure_ascii=False)

            print(f"Sorted entries in: {full_path}")

        except json.JSONDecodeError:
            print(f"Invalid JSON in {full_path}, skipping.")
        except Exception as e:
            print(f"Error processing {full_path}: {e}")
