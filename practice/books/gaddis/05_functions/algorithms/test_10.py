from typing import TypeVar

T = TypeVar('T')


def get_first_name(name: T) -> T:
    return name


def test_get_first_name():
    assert get_first_name('alex') == 'alex'
    assert get_first_name('maria') == 'maria'
