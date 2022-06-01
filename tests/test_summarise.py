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
