import sys

s1 = sys.intern('value1')
s2 = sys.intern('value1')

a = '12'
b = '1' + '2'
print(a is b)

a = '12'
b = ''.join(['1', '2'])
print(a is b)

a = [1, 2]
b = [1, 2]
print(a is b)

# integer caching
a = 2
b = 1 + 1
print(a is b)


# immutable caching
a = (1,)
b = (1,)

print(a is b)
