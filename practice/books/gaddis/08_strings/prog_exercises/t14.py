from decimal import Decimal

FILENAME = 'GasPrices.txt'
DATE_PRICE_SPLITTER = ':'
DATE_PARTS_SPLITTER = '-'


def calc_average_prices_for_years(data: list) -> list:
    if not data:
        raise ValueError("There aren't data")

    current_year = data[0][0]
    year_average_prices = []
    tmp_year_prices = []

    for year, month, day, price in data:
        if current_year == year:
            tmp_year_prices.append(price)
        else:
            current_year = year
            year_average_prices.append(
                [year, sum(tmp_year_prices) / len(tmp_year_prices)]
            )
            tmp_year_prices.clear()

    return year_average_prices


def main() -> None:
    data = []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            date, price = line.split(DATE_PRICE_SPLITTER)
            day, month, year = date.split(DATE_PARTS_SPLITTER)

            price = Decimal(price)

            data.append([year, month, day, price])

    print('*** average prices by years ***')
    for year, price in calc_average_prices_for_years(data):
        print(f'{year}: {price}')
    print('*' * 31)


if __name__ == '__main__':
    main()
