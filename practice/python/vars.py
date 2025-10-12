# Распаковка
a, b, c = 1, 2, 3

# Множественное присваивание
a = b = c = None

# id
print(
    id(a) == id(b),
    id(a),
    id(None),
)


def foo():
    foo_var = 1

    print(locals())
    print(globals())


foo()

print(
    2 == 1,
    [1, 2] == [1, 2],
    foo is a,
)
