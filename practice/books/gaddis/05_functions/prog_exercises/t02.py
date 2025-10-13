def calc_tax(total: float, interest: int) -> float:
    tax = total * (interest / 100)

    return round(tax, 2)
