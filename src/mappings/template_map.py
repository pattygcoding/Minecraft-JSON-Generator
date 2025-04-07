from src.mappings.helpers.template_map_helpers import *

block = {
    "templates": [
        blockstate(),
        model_block(),
        model_item("block"),
        loot_table("block"),
    ]
}

block_gemblock = {
    "templates": block["templates"] + [
        advancement("recipes/building_blocks/gemblock"),
        recipe("gemblock"),
        tag("blocks/beacon_base_blocks")
    ]
}

item = {
    "templates": [
        model_item()
    ]
}

item_gem = {
    "templates": item["templates"] + [
        recipe("gem"),
        advancement("recipes/misc/gem"),
        tag("items/beacon_payment_items")
    ]
}

template_map = {
    "block": block,
    "block/gemblock": block_gemblock,
    "item": item,
    "item/gem": item_gem
}
