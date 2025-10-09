def times_ten(num: int) -> int:
    return num * 10


def test_times_ten():
    assert times_ten(2) == 20
    assert times_ten(3) == 30
