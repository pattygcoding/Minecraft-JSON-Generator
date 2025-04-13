import os
from src.mappings.tag_map import tag_map

def delete_all(mod_name):
    resources_dir = "resources"
    deleted_files = []

    # Get exclusion mapping
    exclusions = tag_map(mod_name)

    for root, _, files in os.walk(resources_dir):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, resources_dir)

                if rel_path in exclusions:
                    new_content = exclusions[rel_path]
                    try:
                        os.makedirs(os.path.dirname(file_path), exist_ok=True)
                        if not os.path.exists(file_path):
                            # File doesn't exist, create it
                            with open(file_path, "w") as f:
                                f.write(new_content)
                            print(f"Created (preserved): {file_path}")
                        else:
                            # File exists, only rewrite if content differs
                            with open(file_path, "r") as f:
                                current_content = f.read()
                            if current_content != new_content:
                                with open(file_path, "w") as f:
                                    f.write(new_content)
                                print(f"Rewritten (preserved): {file_path}")
                    except Exception as e:
                        print(f"Failed to rewrite {file_path}: {e}")
                    continue

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
