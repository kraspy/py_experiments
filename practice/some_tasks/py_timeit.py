import timeit
import time


NUM_ITERATIONS = 1_000_000
PRECISION = '.3f'

some_var = 'Hello'


def fstring_format():
    f'{some_var}'


def str_format():
    '{0}'.format(some_var)


def printf():
    '%s' % (some_var)


print(f'f-string: {timeit.timeit(fstring_format, number=NUM_ITERATIONS):{PRECISION}}s')
print(f'format(): {timeit.timeit(str_format, number=NUM_ITERATIONS):{PRECISION}}s')
print(f'printf %: {timeit.timeit(printf, number=NUM_ITERATIONS):{PRECISION}}s')


print(timeit.repeat(fstring_format, repeat=10, number=NUM_ITERATIONS))

timer = timeit.Timer('len(x)', setup='x = [i for i in range(10_000_000)]')

print(timer.timeit(number=1000000))

print(timer.autorange())


print(f'default_timer: {timeit.default_timer}')
print(f'default_timer(): {timeit.default_timer()}')
print(f'time.perf_counter: {time.perf_counter()}')
