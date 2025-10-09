from decimal import DivisionByZero

import pytest


# ========================================
# BASIC ASSERTION
# ========================================
def add_numbers(*args):
    return sum(args)


def test_add_numbers():
    assert add_numbers(1, 2, 3) == 6, 'Тут должно быть 6'
    assert add_numbers(3, 2, 1) == 6, 'Тут должно быть 6'
    assert add_numbers(1) == 1, 'Тут должно быть 1'


# ========================================
# RAISES
# ========================================
def division(a, b):
    return a / b


def test_raises():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

    with pytest.raises(Exception, match=r'.*zer.+'):
        division(1, 0)

    with pytest.raises(Exception) as exc_info:
        division(1, 0)

    assert 'zero' in str(exc_info.value)  # Обязательно приводить к строке
