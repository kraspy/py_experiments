class MyIterator:
    def __init__(self) -> None:
        self._values = 'a b c d e f'.split(' ')
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index >= len(self._values):
            raise StopIteration
        else:
            self._current_index += 1
            return self._values[self._current_index - 1]


it = MyIterator()

for el in it:
    print(el, end=' ')
