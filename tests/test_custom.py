import pytest

from validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_1(validator):
    # Метод добавления новых валидаторов
    # add_validator(type, name, fn)
    validator.add_validator(
        'string',
        'startWith',
        lambda value, start: value.startswith(start)
    )

    # Новые валидаторы вызываются через метод test
    schema = validator.string().test('startWith', 'H')
    assert schema.is_valid('exlet') is False
    assert schema.is_valid('Hexlet') is True

    validator.add_validator(
        'number',
        'min',
        lambda value, min: value >= min
    )

    schema = validator.number().test('min', 5)
    assert schema.is_valid(4) is False
    assert schema.is_valid(6) is True
