import os
import re
from decimal import Decimal
import json

def sanitize_filename(value):
    value = str(value)
    value = re.sub(r"[^\w\s-]", "", value)
    value = re.sub(r"\s+", "_", value.strip())
    return value[:50] or "unnamed"

def fallback(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def ensure_output_folder(path):
    os.makedirs(path, exist_ok=True)

def write_json_file(obj, path):
    with open(path, "w", encoding="utf-8") as out:
        json.dump(obj, out, indent=2, default=fallback)

def get_directory():
    input_path = input("Please enter the folder location of the chat file.\n")
    filepath = os.path.join(input_path, "conversations.json")
    output_directory = os.path.join(input_path, "chats-history")
    return filepath, output_directory
