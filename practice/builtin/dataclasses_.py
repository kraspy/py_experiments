from dataclasses import dataclass, field, InitVar, asdict


@dataclass(frozen=False, eq=True, unsafe_hash=True)
class SomeData:
    """It is a docstring for Some Class"""

    url: str
    access_level: int = field(
        repr=False,
    )
    items: list = field(default_factory=list, compare=False)
    some_var: InitVar[str] = '123'

    def __post_init__(self, v):
        if self.access_level > 2:
            raise ValueError('Access level must be less or equal than 2')


sd = SomeData('https://url.ru', 2)
sd.items.extend([1, 2, 3])

print(sd)

s = {sd}
sd.items.extend([4, 5, 6])

print(sd.__match_args__)
print(asdict(sd))
help(sd)
