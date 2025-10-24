with open('USPopulation.txt') as f:
    population_list = [int(p.strip()) for p in f.readlines()]

changes_population = [
    population_list[i + 1] - population_list[i] for i in range(len(population_list) - 1)
]


print('Статистика по населению США с 1950 по 1990 год', end='\n\n')
print(
    f'Среднегодовое изменение населения: {round(sum(changes_population) / len(changes_population))}'
)

max_population_index = changes_population.index(max(changes_population))
year_of_max_population = 1950 + max_population_index

print(
    f'Наибольшее увеличение было в {year_of_max_population} году ({changes_population[max_population_index]})'
)

min_population_index = changes_population.index(min(changes_population))
year_of_min_population = 1950 + min_population_index
print(
    f'Наименьшее увеличение было в {year_of_min_population} году ({changes_population[min_population_index]})'
)
