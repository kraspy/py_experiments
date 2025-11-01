import pytest

from t05 import PhoneConverter


@pytest.mark.parametrize(
    'input, expected',
    [
        ('123-GET-FOOD', '123-438-3663'),
        ('123-456-7890', '123-456-7890'),
        ('GET-GET-GETT', '438-438-4388'),
    ],
)
def test_corrent_inputs(input, expected):
    converter = PhoneConverter(input)
    assert converter.convert() == expected


def test_incorrect_input():
    with pytest.raises(ValueError):
        converter = PhoneConverter('1234')
        converter.convert()

    with pytest.raises(ValueError):
        converter = PhoneConverter('123-1234')
        converter.convert()

    with pytest.raises(ValueError):
        converter = PhoneConverter('123-1234-456#')
        converter.convert()
