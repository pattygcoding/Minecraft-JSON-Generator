import os
from src.mappings.clearfiles_map import get_clearfiles_map

def delete_all_json_in_resources(mod_name):
    resources_dir = "resources"
    deleted_files = []

    # Get exclusion mapping
    exclusions = get_clearfiles_map(mod_name)

    for root, _, files in os.walk(resources_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)

                # Compute relative path from 'resources' root
                rel_path = os.path.relpath(file_path, resources_dir)

                # If it's in the exclusions map, rewrite instead of delete
                if rel_path in exclusions:
                    try:
                        with open(file_path, "w") as f:
                            f.write(exclusions[rel_path])
                        print(f"Rewritten (preserved): {file_path}")
                    except Exception as e:
                        print(f"Failed to rewrite {file_path}: {e}")
                    continue

                # Otherwise, delete
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

    if deleted_files:
        print(f"\nDeleted {len(deleted_files)} JSON files:")
        for path in deleted_files:
            print(f" - {path}")
    else:
        print("\nNo JSON files found to delete (excluding mapped exclusions).")
