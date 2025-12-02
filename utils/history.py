import json
import os

HISTORY_FILE = "history.json"

def save_history(algorithm, mode, input_text, key, output):
    data = {
        "algorithm": algorithm,
        "mode": mode,
        "input": input_text,
        "key": key,
        "output": output
    }

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []
