import os
from src.mappings.helpers.tag_map_helpers import *

def tag_map(mod_name):
    return {
        os.path.join("assets", mod_name, "lang", "en_us.json"): JSON_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "mineable/axe.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "mineable/pickaxe.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "mineable/shovel.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "needs_iron_tool.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "needs_stone_tool.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "blocks", "beacon_base_blocks.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "items", "beacon_payment_items.json"): TAG_FORMAT,
        os.path.join("data", "minecraft", "tags", "items", "trimmable_armor.json"): TAG_FORMAT,
    }

def get_tag_keys(mod_name):
    return list(tag_map(mod_name).keys())
