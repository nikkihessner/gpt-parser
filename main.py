from utils.io_helpers import get_directory
from parsers.split_conversations import parse_conversations_file

if __name__ == "__main__":
    filepath, output_folder = get_directory() 

    parse_conversations_file(filepath, output_folder, name_key_title="title", name_key_create="create_time")

