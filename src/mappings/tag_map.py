import os
import json
from src.mappings.helpers.tag_map_helpers import *

def tag_file_list_to_load(filename):
    with open(os.path.join("mappings", "tags", filename)) as f:
        return json.load(f)
    
def tag_map(mod_name):
    base = {
        os.path.join("assets", mod_name, "lang", "en_us.json"): JSON_FORMAT,
    }

    for tag in tag_file_list_to_load("blocks.json"):
        path = os.path.join("data", "minecraft", "tags", "blocks", f"{tag}.json")
        if path not in base:
            base[path] = TAG_FORMAT
    
    for tag in tag_file_list_to_load("items.json"):
        path = os.path.join("data", "minecraft", "tags", "items", f"{tag}.json")
        base[path] = TAG_FORMAT

    return base

def get_tag_keys(mod_name):
    return list(tag_map(mod_name).keys())
