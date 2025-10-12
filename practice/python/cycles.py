a = 1

while a < 5:
    a += 1

    if a == 2:
        continue
    # if a == 4:
    #     break
else:
    print('While finished succesfully')


class MyIterator:
    def __init__(self) -> None:
        self._start = 0
        self._stop = 5

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._stop:
            self._start += 1
            return self._start
        else:
            raise StopIteration


it = MyIterator()

for el in it:
    print(el, end='')
else:
    print('\nFor was iterated successfully')
