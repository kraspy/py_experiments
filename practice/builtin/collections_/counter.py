from collections import Counter

print(c := Counter('aaabbc'))


print(
    c.most_common(n=2),
    c.elements(),
    sep='\n',
)
