import pytest


def main():
    x = 1
    y = 3.4
    print(x, y)
    change_us(x, y)
    print(x, y)


def change_us(a: int, b: float):
    a = 0
    b = 0
    print(a, b)


main()


def test_main(capsys: pytest.CaptureFixture[str]):
    main()
    captured = capsys.readouterr()
    assert captured.out == '1 3.4\n0 0\n1 3.4\n'
