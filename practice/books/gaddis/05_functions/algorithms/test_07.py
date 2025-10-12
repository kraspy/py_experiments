def half(number: float) -> float:
    return number / 2


def test_half():
    result = half(3.0)
    assert result == 1.5
