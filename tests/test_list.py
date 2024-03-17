import pytest

from validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_schema_independence(validator):
    schema = validator.list()
    schema2 = validator.list()
    assert schema != schema2

    schema.required()
    assert schema2.is_valid(None) is True


def test_default(validator):
    schema = validator.list()
    assert schema.is_valid(None) is True
    assert schema.is_valid([1, 3, 4]) is True
    assert schema.is_valid((1, 3, 4)) is True


def test_required(validator):
    schema = validator.list()
    schema.required()
    assert schema.is_valid(None) is False
    assert schema.is_valid(8) is False
    assert schema.is_valid([1, 2, 3]) is True
    assert schema.is_valid((1, 2)) is False
    assert schema.is_valid([]) is True
    assert schema.is_valid(['hexlet']) is True


def test_sizeof(validator):
    schema = validator.list()
    schema.sizeof(2)
    assert schema.is_valid([-6]) is False
    assert schema.is_valid([-5, -5]) is True
    assert schema.is_valid([]) is False
    assert schema.is_valid([5, 5, 5]) is False
    schema.sizeof(0)
    assert schema.is_valid([]) is True
    assert schema.is_valid([1]) is False


def test_fluent(validator):
    schema = validator.list()
    assert schema.required().sizeof(2).is_valid([2, 5]) is True
    assert validator.list().required().is_valid(None) is False
