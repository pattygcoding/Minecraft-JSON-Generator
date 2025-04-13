import os
from mappings.lib import getJsonMap

def asset_model(path):
    return f"resources/assets/{{mod_name}}/models/{path}"

def asset_inventory():
    return f"resources/assets/{{mod_name}}/items"

def data_path(path):
    return f"resources/data/{{mod_name}}/{path}"

def tag_append(path, value_format="{mod_name}:{id}"):
    return {
        "tag_append": path,
        "value_format": value_format
    }

def format_path(path):
    return f"formats/{path}"

def recipe(name):
    def inner(**kwargs):
        item_id = kwargs.get("id", "")
        is_wooden = kwargs.get("wooden", False)

        source_name = f"wooden_{name}" if is_wooden and name in getJsonMap("types", "wooden") else name

        return {
            "source": format_path(f"data/recipes/{source_name}.json"),
            "output": data_path("recipes"),
            "dynamic_filename": f"{item_id}"
        }
    
    return inner


def advancement(path):
    return {
        "source": format_path(f"data/advancements/{path}.json"),
        "output": data_path(f"advancements/{path.rsplit('/', 1)[0]}")
    }

def loot_table(name="block"):
    return {
        "source": format_path(f"data/loot_tables/blocks/{name}.json"),
        "output": data_path("loot_tables/blocks")
    }

def model_item(name="item"):
    return {
        "source": format_path(f"assets/models/item/{name}.json"),
        "output": asset_model("item")
    }

def model_block(name="block"):
    names = [name] if isinstance(name, str) else name
    return [
        {
            "source": format_path(f"assets/models/block/{n}.json"),
            "output": asset_model("block"),
            "model_name_suffix": n
        }
        for n in names
    ]


def blockstate(name="block"):
    return {
        "source": format_path(f"assets/blockstates/{name}.json"),
        "output": f"resources/assets/{{mod_name}}/blockstates"
    }
    
def tag(tag_path, value_format="{mod_name}:{id}"):
    return {
        "tag_append": f"resources/data/minecraft/tags/{tag_path}.json",
        "value_format": value_format
    }

def extend(base, additional):
    return base["templates"] + additional

def inventory(name="item"):
    return {
        "source": format_path(f"assets/items/{name}.json"),
        "output": asset_inventory()
    }