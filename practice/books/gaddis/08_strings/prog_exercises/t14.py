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
            year_average_prices.append(
                [current_year, sum(tmp_year_prices) / len(tmp_year_prices)]
            )
            current_year = year
            tmp_year_prices.clear()

    return year_average_prices


def calc_average_prices_for_years_month(data: list) -> list:
    if not data:
        raise ValueError("There aren't data")

    current_year, current_month = data[0][:2]
    month_average_prices = []
    tmp_months_prices = []

    for year, month, day, price in data:
        if current_year == year and current_month == month:
            tmp_months_prices.append(price)
        else:
            month_average_prices.append(
                [
                    current_year,
                    current_month,
                    sum(tmp_months_prices) / len(tmp_months_prices),
                ]
            )

            current_year = year
            current_month = month
            tmp_months_prices.clear()

    return month_average_prices


def main() -> None:
    data = []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        for line in f:
            date, price = line.split(DATE_PRICE_SPLITTER)
            month, day, year = date.split(DATE_PARTS_SPLITTER)

            price = Decimal(price)

            data.append([year, month, day, price])

    print('*** average prices by years ***')
    for year, price in calc_average_prices_for_years(data):
        print(f'{year}: {price:.2f}')
    print('*' * 31)

    print()

    print('*** average prices by months ***')
    for year, month, price in calc_average_prices_for_years_month(data):
        print(f'{year}/{month}: {price:.2f}')
    print('*' * 31)

    prices = calc_average_prices_for_years(data)

    print('*** sorted prices (ascending) ***')
    for year, price in sorted(prices, key=lambda x: float(x[1])):
        print(f'{year}: {price:.2f}')
    print('*' * 31)

    print('*** sorted prices (descending) ***')
    for year, price in sorted(prices, key=lambda x: float(x[1]), reverse=True):
        print(f'{year}: {price:.2f}')
    print('*' * 31)


if __name__ == '__main__':
    main()
