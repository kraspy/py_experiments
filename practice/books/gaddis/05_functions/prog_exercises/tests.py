from .t01 import convert_km_to_miles
from .t02 import calc_tax


def test_convert_km_to_miles():
    assert convert_km_to_miles(1) == 0.6214


def test_calc_tax():
    assert calc_tax(100, 13) == 13.00
