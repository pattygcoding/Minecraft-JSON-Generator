import os
from src.mappings.tag_map import tag_map

def delete_all_json_in_resources(mod_name):
    resources_dir = "resources"
    deleted_files = []

    # Get exclusion mapping
    exclusions = tag_map(mod_name)

    for root, _, files in os.walk(resources_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)

                # Compute relative path from 'resources' root
                rel_path = os.path.relpath(file_path, resources_dir)

                # If it's in the exclusions map, rewrite instead of delete
                if rel_path in exclusions:
                    try:
                        os.makedirs(os.path.dirname(file_path), exist_ok=True)
                        with open(file_path, "w") as f:
                            f.write(exclusions[rel_path])
                        print(f"Rewritten (preserved): {file_path}")
                    except Exception as e:
                        print(f"Failed to rewrite {file_path}: {e}")
                    continue

                # Otherwise, delete the file
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

    # Ensure excluded files exist (create if missing)
    for rel_path, content in exclusions.items():
        abs_path = os.path.join(resources_dir, rel_path)
        if not os.path.exists(abs_path):
            try:
                os.makedirs(os.path.dirname(abs_path), exist_ok=True)
                with open(abs_path, "w") as f:
                    f.write(content)
                print(f"Created missing excluded file: {abs_path}")
            except Exception as e:
                print(f"Failed to create excluded file {abs_path}: {e}")
