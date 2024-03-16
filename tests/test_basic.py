import pytest

from validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_schema_independence(validator):
    schema = validator.string()
    schema2 = validator.string()
    assert schema != schema2

    schema.required()
    assert schema2.is_valid(None) is True


def test_default(validator):
    schema = validator.string()
    assert schema.is_valid('') is True
    assert schema.is_valid(None) is True
    assert schema.is_valid('what does the fox say') is True


def test_required(validator):
    schema = validator.string()
    schema.required()
    assert schema.is_valid('') is False
    assert schema.is_valid(None) is False
    assert schema.is_valid('what does the fox say') is True


def test_contains(validator):
    schema = validator.string()
    schema.contains("what")
    assert schema.is_valid('what does the fox say') is True
    assert schema.is_valid('hello') is False
    schema.contains("hello")
    assert schema.is_valid('what does the fox say') is False
    assert schema.is_valid('hello') is True


def test_min_length(validator):
    schema = validator.string()
    schema.min_len(6)
    assert schema.is_valid('1234') is False
    assert schema.is_valid('123456789') is True


def test_fluent(validator):
    schema = validator.string()
    assert schema.contains('what').is_valid('what does the fox say') is True
    assert validator.string().min_len(10).min_len(4).is_valid('Hexlet') is True
