# __bool__()
#       => __len__()
#       => True
class MyClass:
    def __len__(self):
        print('MyClass [__len__]')
        return 0


obj = MyClass()
print(bool(obj))


# __str__
#      => __repr__
class MyClass:
    def __repr__(self):
        print('MyClass [__repr__]')
        return self.__class__.__name__


obj = MyClass()
print(obj)


# Полноценный итератор
class MyIter:
    def __init__(self, n: int):
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < 10:
            self.n += 1
            return self.n
        else:
            raise StopIteration


my_iter = MyIter(10)

for current in my_iter:
    print(current, end='')
    print()


# __iter__
#       => __getitem__
class MyGetItemIter:
    def __init__(self, n: int) -> None:
        self.n = n

    def __getitem__(self, index: int):
        if index > self.n:
            raise IndexError
        print(f'MyGetItemIter [__getitem__]: {index=}')
        return index + 1


my_getitem_iter = MyGetItemIter(5)

for i in my_getitem_iter:
    print(i)


# in
class MyContainer:
    def __contains__(self, item):
        print(f'MyContainer [__contains__]: {item=}')
        return item == 1


obj = MyContainer()

print(1 in obj)


# __radd__
#       => __add__
# Если __add__ возвращает `NotImplemented`, вызывается __radd__
class Addable:
    def __add__(self, other):
        print('__add__ called')
        return Addable()

    def __radd__(self, other):
        print('__radd__ called')
        return Addable()


a = Addable()
b = Addable()
a + b  # Вызывает __add__
5 + a  # Вызывает __radd__
