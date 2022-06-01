import pytest

from json_summary import summarise


def test_summarise() -> None:
    with pytest.raises(Exception):
        summarise("blah")

    assert summarise({"name": "foo"}) == {"name": "string"}

    assert summarise({"name": "John Doe", "age": 15, "height": 155.5, "graduated": False, "address": None}) == {
        "name": "string",
        "age": "number",
        "height": "number",
        "graduated": "boolean",
        "address": "null",
    }

    assert summarise([1, "foo", True, 2.5, None, False]) == ["number", "string", "boolean", "number", "null", "boolean"]
