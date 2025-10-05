price_for_year: float = 145_000
year_exceed_percent = 0.03

total_price = 0.0
for year in range(1, 6):
    if year >= 2:
        price_for_year += price_for_year * year_exceed_percent

    total_price += round(price_for_year, 2)

    print(f'Year {year}: {price_for_year:.2f}')

print(f'🏁 Total: {total_price:.2f}')
