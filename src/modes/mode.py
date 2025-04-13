import sys
import json

def mode():
    if "--changeModName" in sys.argv:
        from src.modes.change_mod_name.change_mod_name import change_mod_name
        change_mod_name()
        return True

    if "--delete" in sys.argv:
        from src.modes.delete_all.delete_all import delete_all
        with open("config/modname.json", "r") as f:
            config = json.load(f)
        mod_name = config.get("mod_name")
        delete_all(mod_name)
        return True

    if "--sortTags" in sys.argv:
        from src.modes.sort_tags.sort_tags import sort_tag_files
        with open("config/modname.json", "r") as f:
            config = json.load(f)
        mod_name = config.get("mod_name")
        sort_tag_files(mod_name)
        return True

    return False
