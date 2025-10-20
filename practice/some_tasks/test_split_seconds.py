import pytest
from split_seconds_to_H_M_S import format_seconds


@pytest.mark.parametrize(
    'input, expected',
    [
        (0, (0, 0, 0)),  # ноль секунд
        (1, (0, 0, 1)),  # базовый случай
        (59, (0, 0, 59)),  # верхняя граница секунд
        (60, (0, 1, 0)),  # ровно одна минута
        (61, (0, 1, 1)),  # минута + секунда
        (3599, (0, 59, 59)),  # последняя секунда перед часом
        (3600, (1, 0, 0)),  # ровно один час
        (3665, (1, 1, 5)),  # больше часа
        (86399, (23, 59, 59)),  # верхняя граница перед "сутками"
        (86400, (24, 0, 0)),  # часы накапливаются, дни не считаем
        (10**6, (277, 46, 40)),  # крупное значение
    ],
)
def test_split_seconds(input, expected):
    assert format_seconds(input) == expected


def test_type_exception_split_seconds():
    with pytest.raises(TypeError):
        format_seconds('1')


def test_value_exception_split_seconds():
    with pytest.raises(ValueError):
        format_seconds(-1)
