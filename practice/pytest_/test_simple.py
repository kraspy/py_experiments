import pytest


# ========================================
# BASIC ASSERTION
# ========================================
def add_numbers(*args: int):
    return sum(args)


def test_add_numbers():
    assert add_numbers(1, 2, 3) == 6, 'Тут должно быть 6'
    assert add_numbers(3, 2, 1) == 6, 'Тут должно быть 6'
    assert add_numbers(1) == 1, 'Тут должно быть 1'


# ========================================
# RAISES
# ========================================
def division(a: int, b: int) -> float:
    return a / b


def test_raises():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

    with pytest.raises(Exception, match=r'.*zer.+'):
        division(1, 0)

    with pytest.raises(Exception) as exc_info:
        division(1, 0)

    assert 'zero' in str(exc_info.value)  # Обязательно приводить к строке


# ========================================
# PARAMS
# ========================================
@pytest.mark.parametrize(
    'a, b, expected',
    (
        (1, 2, 2),
        (2, 2, 4),
        (3, 2, 6),
    ),
    ids=['first', 'second', 'third'],
)
def test_multiple(a: int, b: int, expected: int):
    assert a * b == expected


# функция в ids
def ids_fn(value: str):
    return repr(value)


@pytest.mark.parametrize(
    'a, b, expected',
    (
        (1, 1, 2),
        (2, 2, 4),
    ),
    ids=ids_fn,
)
def test_add(a: int, b: int, expected: int):
    assert a + b == expected


# ========================================
# MARKERS
# ========================================

# pytest -m "not slow"
# pytest -m "not slow"


@pytest.mark.slow
def test_slow():
    assert 1 + 1 == 2


@pytest.mark.network
def test_network():
    assert 2 + 2 == 4


@pytest.mark.skip(reason='просто пропустить')
def test_skip():
    assert 1 + 1 == 2


@pytest.mark.skipif(True, reason='Пропустить по условию')
def test_skipif():
    assert 1 + 1 == 2


@pytest.mark.xfail(reason='Тут ошибка', strict=False)
def test_xfail():
    assert 1 + 1 == 2
