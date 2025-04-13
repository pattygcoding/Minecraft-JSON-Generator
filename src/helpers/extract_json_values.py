import os

def extract_json_values(templates, default_advancements):
    suffixes = set()

    for t in templates:
        source_path = t.get("source", "")
        if "/recipes/" in source_path and source_path.endswith(".json"):
            suffix = os.path.splitext(os.path.basename(source_path))[0]

            if suffix == "default":
                for folder, mapping in default_advancements.items():
                    if f"/{folder}/" in source_path:
                        if isinstance(mapping, dict):
                            for keyword, resolved in mapping.items():
                                if keyword != "default" and keyword in source_path:
                                    suffix = resolved
                                    break
                            else:
                                suffix = mapping.get("default", "item")
                        else:
                            suffix = mapping
                        break
                else:
                    suffix = default_advancements.get("default", "item")

            suffixes.add(suffix)

    return suffixes
