import ijson

def stream_conversations(filepath):
    with open(filepath, "rb") as f:
        for item in ijson.items(f, "item"):
            yield item