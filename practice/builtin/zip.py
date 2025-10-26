from itertools import zip_longest


print(
    list(
        zip(
            range(5),
            ['a', 'b', 'c', 'd', 'e', 'F'],
            # strict=True,
        )
    )
)


print(
    list(
        zip(
            *enumerate('abcde'),
        )
    )
)


print(
    list(
        zip_longest(
            range(5),
            ['a', 'b', 'c', 'd', 'e', 'F'],
        )
    )
)
