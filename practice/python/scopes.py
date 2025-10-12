# LEGB


# global
x = 1


def foo():
    # enclosing
    x = 2
    print(f'Enclosing: {x}')

    def bar():
        # local
        x = 3
        print(f'Local: {x}')
        return x

    return bar


# built-in
print('Built-in', len)
print('Global:', x)

outer = foo()
inner = outer()


def change_global_x():
    global x

    x = 10


change_global_x()

print(f'{x=}')


def change_nonlocal_var():
    x = 0

    def inner():
        nonlocal x

        x = 10

    inner()
    return x


print('Changed nonlocal var:', change_nonlocal_var())
