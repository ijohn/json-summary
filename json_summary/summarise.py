from typing import Any


def _get_value_repr(value: Any) -> str:
    if value is None:
        return "null"

    if isinstance(value, str):
        return "string"

    if isinstance(value, bool):
        return "boolean"

    if isinstance(value, (int, float)):
        return "number"

    raise Exception(f"Unknown type for value {value}")  # pragma: no cover


def _get_obj_repr(value: Any, depth: int, max_depth: int | None = None) -> Any:
    if max_depth is not None:
        if depth < max_depth:
            return _process_dict(value, depth, max_depth=max_depth)

        return {}

    return _process_dict(value, depth, max_depth=max_depth)


def _get_arr_repr(value: Any, depth: int, max_depth: int | None = None) -> Any:
    if max_depth is not None:
        if depth < max_depth:
            return _process_list(value, depth, max_depth=max_depth)

        return []

    return _process_list(value, depth, max_depth=max_depth)


def _process_dict(in_dict: Any, depth: int, max_depth: int | None = None) -> Any:
    result = {}
    depth += 1

    for key, value in in_dict.items():
        if isinstance(value, dict):
            result[key] = _get_obj_repr(value, depth, max_depth=max_depth)
            continue

        if isinstance(value, list):
            result[key] = _get_arr_repr(value, depth, max_depth=max_depth)
            continue

        result[key] = _get_value_repr(value)

    return result


def _process_list(in_list: Any, depth: int, max_depth: int | None = None) -> Any:
    result = []
    depth += 1

    for elem in in_list:
        if isinstance(elem, dict):
            result.append(_get_obj_repr(elem, depth, max_depth=max_depth))
            continue

        if isinstance(elem, list):
            result.append(_get_arr_repr(elem, depth, max_depth=max_depth))
            continue

        result.append(_get_value_repr(elem))

    return result


def summarise(in_json: Any, max_depth: int | None = None) -> Any:
    if isinstance(in_json, dict):
        return _process_dict(in_json, 0, max_depth=max_depth)

    if isinstance(in_json, list):
        return _process_list(in_json, 0, max_depth=max_depth)

    raise Exception("Invalid JSON")
