import pytest

from validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_schema_independence(validator):
    schema = validator.dict()
    schema2 = validator.dict()
    assert schema != schema2


def test_1(validator):
    schema = validator.dict()
    schema.shape({
        'name': validator.string().required(),
        'age': validator.number().positive(),
    })

    assert schema.is_valid({'name': 'kolya', 'age': 100}) is True
    assert schema.is_valid({'name': 'maya', 'age': None}) is True
    assert schema.is_valid({'name': '', 'age': None}) is False
    assert schema.is_valid({'name': 'ada', 'age': -5}) is False
