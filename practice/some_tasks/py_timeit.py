import timeit
import time

approaches = (
    ('f-string', "f'{name}'"),
    ('format()', "'{name}'.format(name=name)"),
    ('printf %:', "'%s' % name"),
)

print('*' * 10 + 'timeit' + '*' * 10)
for name, stmt in approaches:
    result = timeit.timeit(stmt, number=10000, setup="name = 'Evgeniy'")
    print(f'{name}: {result}s')
print('*' * 10 + 'timeit' + '*' * 10, end='\n')

for name, stmt in approaches:
    result = timeit.repeat(stmt, repeat=5, setup="name = 'Evgeniy'")
    print(f'{name}: {result}')

timer = timeit.Timer('len(x)', setup='x = [i for i in range(10_000_000)]')

print(timer.timeit(number=1000000))

print(timer.autorange())
