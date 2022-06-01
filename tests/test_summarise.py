import pytest

from json_summary import summarise


def test_raise_on_invalid_json() -> None:
    with pytest.raises(Exception):
        summarise("blah")

    with pytest.raises(Exception):
        summarise(None)


def test_empty_obj_and_arr() -> None:
    assert summarise({}) == {}
    assert summarise([]) == []


def test_simple_obj_and_arr() -> None:
    assert summarise({"name": "John Doe", "age": 15, "height": 155.5, "graduated": False, "address": None}) == {
        "name": "string",
        "age": "number",
        "height": "number",
        "graduated": "boolean",
        "address": "null",
    }

    assert summarise([1, "foo", True, 2.5, None, False]) == ["number", "string", "boolean", "number", "null", "boolean"]


def test_complex_obj() -> None:
    assert summarise(
        {
            "name": "John Doe",
            "address": {"city": "Jakarta"},
            "friends": [{"name": "Jane Doe", "address": {"city": "Bandung"}}],
        }
    ) == {
        "name": "string",
        "address": {"city": "string"},
        "friends": [{"name": "string", "address": {"city": "string"}}],
    }


def test_complex_arr() -> None:
    assert summarise([10, [True], {"name": "John Doe"}]) == ["number", ["boolean"], {"name": "string"}]


def test_complex_obj_with_max_depth() -> None:
    in_json = {
        "name": "John Doe",
        "address": {"city": "Jakarta"},
        "friends": [{"name": "Jane Doe", "address": {"city": "Bandung"}}],
    }
    assert summarise(in_json) == {
        "name": "string",
        "address": {"city": "string"},
        "friends": [{"name": "string", "address": {"city": "string"}}],
    }
    assert summarise(in_json, max_depth=1) == {"name": "string", "address": {}, "friends": []}
    assert summarise(in_json, max_depth=2) == {
        "name": "string",
        "address": {"city": "string"},
        "friends": [{}],
    }
    assert summarise(in_json, max_depth=3) == {
        "name": "string",
        "address": {"city": "string"},
        "friends": [{"name": "string", "address": {}}],
    }


def test_complex_arr_with_max_depth() -> None:
    in_json = [
        12,
        [True],
        {"name": "John Doe", "address": {"city": "Jakarta"}},
        {"name": "Jane Doe", "address": {"city": "Bandung"}},
    ]
    assert summarise(in_json) == [
        "number",
        ["boolean"],
        {"name": "string", "address": {"city": "string"}},
        {"name": "string", "address": {"city": "string"}},
    ]
    assert summarise(in_json, max_depth=1) == ["number", [], {}, {}]
    assert summarise(in_json, max_depth=2) == [
        "number",
        ["boolean"],
        {"name": "string", "address": {}},
        {"name": "string", "address": {}},
    ]
