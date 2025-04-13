import os
import json

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def replace_in_file(filepath, old, new):
    with open(filepath, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(filepath, "w") as f:
        f.write(content)

def replace_all_in_directory(directory, old, new):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                full_path = os.path.join(root, file)
                replace_in_file(full_path, old, new)

def change_mod_name():
    config = load_json("config/modname.json")
    mod_name = config.get("mod_name")
    new_mod_name = config.get("new_mod_name", "").strip()

    if not new_mod_name:
        raise ValueError("new_mod_name cannot be blank in config/modname.json")

    old_path = os.path.join("resources", "assets", mod_name)
    new_path = os.path.join("resources", "assets", new_mod_name)

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed folder: {old_path} → {new_path}")
    else:
        print(f"Warning: Path {old_path} does not exist. Skipping rename.")

    replace_all_in_directory(new_path, mod_name, new_mod_name)

    config["mod_name"] = new_mod_name
    config["new_mod_name"] = ""
    save_json("config/modname.json", config)

    print(f"Updated config/modname.json with new mod_name: {new_mod_name}")
