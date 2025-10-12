import pytest


def my_function(a: int, b: int, c: int):
    d = (a + c) / b
    print(d)


def test_my_function(capsys: pytest.CaptureFixture[str]):
    my_function(2, 4, 6)

    captured = capsys.readouterr()
    assert captured.out == '2.0\n'
