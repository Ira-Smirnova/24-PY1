import json

IN_FILE = "input.json"


def task(in_file) -> float:
    with open(in_file) as in_f:
        json_data = json.load(in_f)
    return round(sum([item["score"] * item["weight"] for item in json_data]), 3)

print(task(IN_FILE))
