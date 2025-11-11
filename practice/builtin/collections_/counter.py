from collections import Counter

# Definition
print(c := Counter('ababac'))
print(c1 := Counter(a=4, b=3, c=2, d=1))


print(
    c.most_common(n=2),
    list(c.elements()),
    sep='\n',
)

print(f'{" ".join(c1.elements())}')


# Subtraction
print(c1 - c)
c1.subtract(c)
print(c1)


# Update
c1.update('abcd')
print(c1)


# Total - all counts sum
print(c1.total())


# add, sub, intersection, union
print(c1, c)
print(
    c1 + c,
    c1 - c,
    c1 & c,  # min
    c1 | c,  # max
    sep='\n',
)

# unary
print(cu := Counter(a=2, b=0, c=-2))
print(+cu)
print(-cu)


# comparison onjects of Counter
c = Counter('aaabbc')
c1 = Counter('aab')

print(
    c > c1,
    c1 < c,
    c == c1,
)

print(c1.items())
