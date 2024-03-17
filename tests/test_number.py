import pytest

from validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_schema_independence(validator):
    schema = validator.number()
    schema2 = validator.number()
    assert schema != schema2

    schema.required()
    assert schema2.is_valid(None) is True


def test_default(validator):
    schema = validator.number()
    assert schema.is_valid(None) is True
    assert schema.is_valid(7) is True


def test_required(validator):
    schema = validator.number()
    schema.required()
    assert schema.is_valid(None) is False
    assert schema.is_valid(8) is True


def test_positive(validator):
    schema = validator.number()
    schema.positive()
    assert schema.is_valid(None) is True
    assert schema.is_valid(-7) is False
    assert schema.is_valid(0) is False
    assert schema.is_valid(7) is True
    schema.positive()
    assert schema.is_valid(4) is True
    assert schema.is_valid(-4) is True
    assert schema.is_valid(0) is True


def test_range(validator):
    schema = validator.number()
    schema.range(-5, 5)
    assert schema.is_valid(-6) is False
    assert schema.is_valid(-5) is True
    assert schema.is_valid(6) is False
    assert schema.is_valid(5) is True
    assert schema.is_valid(0) is True


def test_fluent(validator):
    schema = validator.number()
    assert schema.positive().is_valid(10) is True
    assert (validator.number().positive().required().positive().is_valid(-10)
            is True)
