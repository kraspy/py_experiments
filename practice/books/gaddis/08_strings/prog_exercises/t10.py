def max_repeated_char(text: str) -> None:
    symbols = []
    repeated = []

    for letter in text:
        if letter not in symbols:
            symbols.append(letter)
            repeated.append(1)
            continue
        repeated[symbols.index(letter)] += 1

    max_repeated_value = max(repeated)
    max_repeated_symbol = symbols[repeated.index(max_repeated_value)]

    print(
        f'Наиболее часто повторяется символ: "{max_repeated_symbol}"\nКоличество повторов: {max_repeated_value}'
    )


max_repeated_char('abcaba!')
