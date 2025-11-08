from random import randint
from collections import Counter, defaultdict

list_of_numbers = [randint(1, 10) for _ in range(1000)]

counter = {}

for i in list_of_numbers:
    counter[i] = counter.get(i, 0) + 1


print(counter)


res = Counter(list_of_numbers)

print(res.total())
print(res.most_common())

print(res)


dict_ = {'a': 1}

dict_.update(**{'b': 2})


print(dict_)

# dd = defaultdict(list)
dd = defaultdict(lambda: {'counter': int(), 'values': list()})

dd['a']['counter'] += 1
dd['a']['values'].append(1)

print(dd)
