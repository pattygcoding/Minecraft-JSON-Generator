import os

def get_clearfiles_map(mod_name):
    return {
        os.path.join("assets", mod_name, "lang", "en_us.json"): "{\n\n}"
    }

def get_clearfiles_keys(mod_name):
    return list(get_clearfiles_map(mod_name).keys())
