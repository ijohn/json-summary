from typing import Any


def get_repr(value: Any) -> str:
    if value is None:
        return "null"

    if isinstance(value, str):
        return "string"

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, (int, float)):
        return "number"

    raise Exception(f"Unknown type for value {value}")  # pragma: no cover


def process_dict(in_dict: Any) -> Any:
    result = {}

    for key, value in in_dict.items():
        if isinstance(value, dict):
            result[key] = process_dict(value)
            continue

        if isinstance(value, list):
            result[key] = process_list(value)
            continue

        result[key] = get_repr(value)

    return result


def process_list(in_list: Any) -> Any:
    result = []

    for elem in in_list:
        if isinstance(elem, dict):
            result.append(process_dict(elem))
            continue

        if isinstance(elem, list):
            result.append(process_list(elem))
            continue

        result.append(get_repr(elem))

    return result


def summarise(in_json: Any) -> Any:
    if isinstance(in_json, dict):
        return process_dict(in_json)

    if isinstance(in_json, list):
        return process_list(in_json)

    raise Exception("Invalid JSON")
