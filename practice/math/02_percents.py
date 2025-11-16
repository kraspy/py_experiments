def print_result(fn):
    def wrapper(*args):
        result = fn(*args)
        print(result)
        return result

    return wrapper


@print_result
def calc_percent(number: int, percent: int) -> float:
    return number * (percent / 100)
    # return number * percent / 100


@print_result
def add_percent(number: int, percent: int) -> float:
    # return number + (number * (percent / 100))
    return number * (1 + percent / 100)


@print_result
def remove_percent(number: int, percent: int) -> float:
    # return number - (number * percent / 100)
    return number * (1 - percent / 100)


calc_percent(100, 5)
calc_percent(150, 50)

add_percent(100, 5)

remove_percent(100, 5)


@print_result
def calc_percent_num_from_num(part: int, whole: int) -> float:
    return (part / whole) * 100


calc_percent_num_from_num(5, 100)


@print_result
def calc_percent_num_more_than_num(old: int, new: int) -> float:
    return ((new - old) / old) * 100


@print_result
def calc_percent_num_less_than_num(old: int, new: int) -> float:
    return ((old - new) / old) * 100


calc_percent_num_more_than_num(100, 120)
calc_percent_num_less_than_num(120, 100)


@print_result
def calc_source_from_add_percent(new: int, percent: int) -> float:
    return new / (1 + (percent / 100))


@print_result
def calc_source_from_remove_percent(new: int, percent: int) -> float:
    return new / (1 - percent / 100)


calc_source_from_add_percent(120, 20)
calc_source_from_remove_percent(80, 20)


@print_result
def compound_interest(number: int, percent: int, years: int) -> float:
    return number * ((1 + (percent / 100)) ** years)


compound_interest(1000, 5, 2)
