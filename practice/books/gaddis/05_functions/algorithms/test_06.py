import random

random.seed(1)


def get_random_int(start: int, stop: int) -> int:
    random_number = random.randint(start, stop)
    return random_number


def test_get_random_int():
    assert get_random_int(1, 100) == 18
