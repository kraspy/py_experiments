from enum import Enum

print(
    abs(-1),
    abs(5),
)
print(
    any([1, 0]),
    any([]),
)
print(
    all([1, 0]),
    all([]),
)
print(
    bin(16),
    oct(16),
    hex(16),
)
print(
    bool(0),
    dict(),
    float(0),
    int(0),
    set([0]),
    str(0),
)
print(callable(bool))
print(ord('A'), chr(65))
print(divmod(3600, 60))
print(list(enumerate(['a', 'b', 'c'])))
print(list(filter(bool, [0, False, 2, 3])))
print(list(map(str, [True, 1, set([1, 2])])))
print(format(1, '-^10'))
print(hasattr(object, 'mro'))
print(setattr(Enum, 'myattr', 'myvalue'))
print(getattr(Enum, 'myattr', '-'))
print(delattr(Enum, 'myattr'))
print(hash(Enum))
print(id(Enum))
print(isinstance(True, int))
print(issubclass(bool, int))
print(iter((1, 2)))
print(len((1, 2)))
print(max(['a', 'ab'], key=len, default=0))
print(min(['a', 'ab'], key=len, default=0))
print(pow(2, 8))
print(
    round(1234.1234, -2),
    round(1234.1234, 2),
    round(3.5),
    round(-3.5),
)
print(sorted((1, 2, 3), reverse=True), reversed([1, 2, 3]))
print(
    sum([1, 2, 3]),
    sum([[1, 2, 3], [4, 5, 6]], []),
)
print(type(bool))
print(list(zip([1, 'a', 3], [2, 'b'])))
