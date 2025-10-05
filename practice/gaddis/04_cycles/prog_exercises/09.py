ocean_up_mm_per_year = 1.6

total_ocean_up_mm = 0

for year in range(25):
    total_ocean_up_mm += ocean_up_mm_per_year
    print(f'Year {year + 1}: {total_ocean_up_mm:.2f} mm')
