import json


def to_json(data: dict) -> str:
    return json.dumps(data, ensure_ascii=False)
