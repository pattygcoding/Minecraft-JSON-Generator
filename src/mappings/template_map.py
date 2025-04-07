template_map = {
    "item": {
        "templates": [
            {
                "source": "formats/items/assets/models.item/item.json",
                "output": "resources/assets/{mod_name}/models/item"
            }
        ]
    },
    "block/gemblock": {
        "templates": [
            {
                "source": "formats/items/assets/blockstates/cube_all.json",
                "output": "resources/assets/{mod_name}/blockstates"
            },
            {
                "source": "formats/items/assets/models/block/cube_all.json",
                "output": "resources/assets/{mod_name}/models/block"
            }
        ]
    }
}
