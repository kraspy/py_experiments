from collections import UserDict, UserList, UserString


class MyDict(UserDict):
    def __getitem__(self, key):
        print(f'Get key: "{key}"')
        return super().__getitem__(key)

    def __setitem__(self, key, item):
        print(f'Set key: "{key}", item: "{item}"')
        return super().__setitem__(key, item)


md = MyDict({'a': 1, 'b': 2})

print(md['a'])
print(md.data)


class MyList(UserList):
    def append(self, item):
        print(f'Item "{item}" appended')
        super().append(item)


ml = MyList([1, 2, 3])
ml.append(4)
print(ml)


class MyStr(UserString):
    def __contains__(self, char: object) -> bool:
        print('MyStr.__contains__ called')
        return super().__contains__(char)


ms = MyStr('123')
print('1' in ms)
