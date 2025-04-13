optional_fields_map = {
    "block/slab": {
        "tool": {
            "axe": "blocks/mineable/axe",
            "hoe": "blocks/mineable/hoe",
            "pickaxe": "blocks/mineable/pickaxe",
            "shovel": "blocks/mineable/shovel"
        }
    },
    "block/gemblock": {
        "pickaxe": {
            "iron": "blocks/needs_iron_tool",
            "stone": "blocks/needs_stone_tool"
        },
        "beacon_block": {
            True: "blocks/beacon_base_blocks"
        }
    },
    "item/gem": {
        "beacon_payment": {
            True: "items/beacon_payment_items"
        }
    }
}
