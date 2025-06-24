import json 
import ijson
import os 
import re
from decimal import Decimal

def sanitize_filename(value):
    value = str(value)
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "_", value.strip())
    return value[:50] or "unnamed"

def fallback(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


if __name__ == "__main__":
    folder = input("Please select the folder containing your ChatGPT history:\n")
    filepath = os.path.join(folder, "conversations.json")
    print(filepath)

    output_folder = input("Please enter output folder destination:\n")
    name_key_title = "title"
    name_key_create = "create_time"

    # Make output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    with open(filepath, "rb") as f:
        parser = ijson.items(f, "item")
        for i, obj in enumerate(parser):
            parser = ijson.items(f, "item")
            name = str(obj.get(name_key_title, f"entry_{i}"))
            create_time = str(obj.get(name_key_create, f"entry_{i}"))
            output_filename = sanitize_filename(name + create_time)
            path = os.path.join(output_folder, f"{output_filename}.json")
            with open(path, "w", encoding="utf-8") as out:
                json.dump(obj, out, indent=2, default=fallback)
    