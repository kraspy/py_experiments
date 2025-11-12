from collections import defaultdict

# definition
dd = defaultdict(list)

# group data example
tmp_data = [('red', 1), ('green', 2), ('red', 2), ('blue', 1)]

for k, v in tmp_data:
    dd[k].append(v)

print(dd)

# complex init
dd = defaultdict(lambda: 0)

dd['int1'] = 5
dd['int2']

print(dd)


# default_factory
print(dd.default_factory)
dd.default_factory = None
# dd['int3']  # KeyError
