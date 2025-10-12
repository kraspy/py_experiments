gen_expr = (i for i in 'abcdef')


def gen_fn(*args):
    for el in args:
        yield el


for i in gen_fn('abcdef'):
    print(i)


# sub_generator
def subgen():
    yield 1
    yield 2


def maingen():
    yield from subgen()
    yield 3


for i in maingen():
    print(i)


def communcative_gen(total=0):
    print('Start...')
    received = yield total
    print(f'{received=}')

    while True:
        if received is None:
            received = 0
        total += received
        print(f'{total=}')
        received = yield total


cgen = communcative_gen()

next(cgen)

print(cgen.send(10))
print(cgen.send(20))
print(cgen.send(30))
