import os

tag_default = (
    '{\n'
    '    "replace": false,\n'
    '    "values": [\n\n    ]\n'
    '}'
)

# Mappings go here
def get_clearfiles_map(mod_name):
    return {
        os.path.join("assets", mod_name, "lang", "en_us.json"): "{\n\n}",
        os.path.join("data", "minecraft", "tags", "items", "beacon_payment_items.json"): tag_default,
        os.path.join("data", "minecraft", "tags", "blocks", "beacon_base_blocks.json"): tag_default
    }

def get_clearfiles_keys(mod_name):
    return list(get_clearfiles_map(mod_name).keys())
