from collections import ChainMap

m0 = {'a': 1}
m1 = {'b': 2}
m2 = {'c': 3}

# definition
cm = ChainMap(m0, m1, m2)
print(list(cm))

# change first element
cm['d'] = 4

print(cm)

defaults = {'theme': 'light', 'lang': 'en'}
root = ChainMap(defaults)

# new_child
context1 = root.new_child({'theme': 'dark'})
context1['a'] = '1'

print(context1)
print(root['theme'])

# parents
print(context1.parents)

# iteration (last -> first)
for el in context1.items():
    print(el)
