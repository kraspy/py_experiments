def cube(num: int) -> int:
    return num * num * num


def test_cube():
    assert cube(3) == 27
    assert cube(2) == 8

    result = cube(4)
    assert result == 64
