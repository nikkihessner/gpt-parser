def parse_conversations_file(filepath, output_folder, name_key_title="title", name_key_create="create_time"):
    from utils.io_helpers import sanitize_filename, ensure_output_folder, write_json_file
    from utils.json_stream import stream_conversations
    import os

    ensure_output_folder(output_folder)

    for i, obj in enumerate(stream_conversations(filepath)):
        name = str(obj.get(name_key_title, f"entry_{i}"))
        create_time = str(obj.get(name_key_create, f"entry_{i}"))
        output_filename = sanitize_filename(create_time + "_" + name)
        output_path = os.path.join(output_folder, f"{output_filename}.json")
        write_json_file(obj, output_path)

