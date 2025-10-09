def show_value(quantity: int) -> int:
    return quantity


def test_show_value():
    assert show_value(10) == 10
    assert show_value(20) == 20
