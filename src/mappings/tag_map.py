import os
from mappings.lib import getJsonMap
from src.mappings.helpers.tag_map_helpers import *

def tag_map(mod_name):
    base = {
        os.path.join("assets", mod_name, "lang", "en_us.json"): JSON_FORMAT,
    }

    for tag in getJsonMap("tags", "blocks"):
        path = os.path.join("data", "minecraft", "tags", "blocks", f"{tag}.json")
        if path not in base:
            base[path] = TAG_FORMAT
    
    for tag in getJsonMap("tags", "items"):
        path = os.path.join("data", "minecraft", "tags", "items", f"{tag}.json")
        base[path] = TAG_FORMAT

    return base

def get_tag_keys(mod_name):
    return list(tag_map(mod_name).keys())
