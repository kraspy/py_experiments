s1 = {1, 2, 3}

s2 = {4, 3, 2, 1}

s3 = {2, 1}

print(
    s1.issuperset(s3),  # >=
    s1.issubset(s2),  # <=
    s1.isdisjoint(s3),  # Нет общих?
    s3.union(s1),  # |
    s1.intersection(s3),  # &
    s1.difference(s3),  # -
    s1.symmetric_difference(s2),  # ^
    sep='\n',
)
