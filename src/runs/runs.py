import sys
import json

def handle_run_flags():
    if "--changeModName" in sys.argv:
        from src.runs.change_mod_name import run_change_mod_name
        run_change_mod_name()
        return True

    if "--delete" in sys.argv:
        from src.runs.delete_all import delete_all_json_in_resources
        with open("config/modname.json", "r") as f:
            config = json.load(f)
        mod_name = config.get("mod_name")
        delete_all_json_in_resources(mod_name)
        return True

    if "--sortTags" in sys.argv:
        from src.runs.sort_tags import sort_tag_files
        with open("config/modname.json", "r") as f:
            config = json.load(f)
        mod_name = config.get("mod_name")
        sort_tag_files(mod_name)
        return True

    return False
