import sys


# Параметры, докстринг
def foo(a, b, *, c, d=30):
    """docstring"""
    return a + b + c + d


foo(1, 2, c=3)

print(sys.getsizeof(foo) + sys.getsizeof(foo.__doc__))

foo.__doc__ = None

print(sys.getsizeof(foo) + sys.getsizeof(foo.__doc__))


def bar(*args, **kwargs):
    print('Args:', args)
    print('KwArgs:', kwargs)


bar(1, 2, 3, a='a', b='b')

bar(*[1, 2, 3])
bar(**{'a': 'a', 'b': 'b'})

print(map(lambda x: len(x), ['a', 'aa', 'aaa']))
