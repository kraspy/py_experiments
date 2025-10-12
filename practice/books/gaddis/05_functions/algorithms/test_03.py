def my_function(a: int, b: int, c: int) -> tuple[int]:
    return a, b, c


def test_my_function():
    assert my_function(3, 2, 1) == (3, 2, 1)
    assert my_function(1, 2, 3) == (1, 2, 3)
