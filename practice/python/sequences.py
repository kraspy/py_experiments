import random


class MySequence:
    def __init__(self) -> None:
        self._values = 'a b c d e f'.split(' ')

    def __len__(self) -> int:
        return len(self._values)

    def __getitem__(self, idx) -> str:
        print(f'[MySequence] getting index: {idx}')
        return self._values[idx]

    def __setitem__(self, idx, value) -> None:
        print(f'[MySequence] setting index: {idx} / value: {value}')
        self._values[idx] = value


seq = MySequence()

print(type(seq))


print(seq[0])

seq[0] = 'A'


print(
    seq[0],
    seq[-1],
    seq[0:2],  # slice
    seq[0:2] + [2, 3],
    sep='\n',
)

print(type(seq[0:2]))

print(
    random.choice(seq),
    random.choices(seq, k=10),
    random.shuffle(seq),
    len(seq),
    seq._values,
    sep='\n',
)

first, *middle, last = seq

print(
    first,
    middle,
    last,
    sep='\n',
)
