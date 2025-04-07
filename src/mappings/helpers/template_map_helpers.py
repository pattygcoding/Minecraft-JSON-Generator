def asset_model(path):
    return f"resources/assets/{{mod_name}}/models/{path}"

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
    return {
        "source": format_path(f"data/recipes/{name}.json"),
        "output": data_path(f"recipes")
    }

def advancement(path):
    return {
        "source": format_path(f"data/advancements/{path}.json"),
        "output": data_path(f"advancements/{path.rsplit('/', 1)[0]}")
    }

def loot_table(name):
    return {
        "source": format_path(f"data/loot_tables/blocks/{name}.json"),
        "output": data_path("loot_tables/blocks")
    }

def model_item(name="item"):
    return {
        "source": format_path(f"assets/models/item/{name}.json"),
        "output": asset_model("item")
    }

def model_block(name="cube_all"):
    return {
        "source": format_path(f"assets/models/block/{name}.json"),
        "output": asset_model("block")
    }

def blockstate(name="cube_all"):
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