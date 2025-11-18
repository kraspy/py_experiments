from dataclasses import (
    KW_ONLY,
    InitVar,
    asdict,
    dataclass,
    field,
    is_dataclass,
    make_dataclass,
)
from typing import ClassVar


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
# help(sd)


# Hashing
@dataclass(frozen=True)
class FrozenDC:
    x: int
    y: int


fdc = FrozenDC(1, 2)

print(hash(fdc))


# Comparison
@dataclass(order=True)
class ComparisonDC:
    x: int
    y: int


cdc0 = ComparisonDC(1, 2)
cdc1 = ComparisonDC(1, 2)

print(cdc0 >= cdc1)


# Unsafe Hash
@dataclass(unsafe_hash=True)
class UnsafeHashDC:
    x: int
    y: int
    z: list = field(default_factory=list, compare=False)


uhdc = UnsafeHashDC(1, 2)

print(hash(uhdc))


# Inheritance
@dataclass
class Animal:
    name: str
    age: int

    def make_sound(self):
        print('...')


@dataclass
class Cat(Animal):
    def make_sound(self):
        print('Meow!')


cat = Cat('Vasyan', 20)

cat.make_sound()


# InitVar
@dataclass
class SomeClass:
    value: int
    noinit_value: InitVar

    def __post_init__(self, initvar_value):
        print(initvar_value, 'is here!')


sc = SomeClass(1, 2)

print(sc)


# key_only attrs
@dataclass  # (kw_only=True)
class WithKeyOnly:
    x: int
    _: KW_ONLY
    y: int  # = field(kw_only=True)


wko = WithKeyOnly(1, y=2)


# __slots__
@dataclass(slots=False)
class WithSlotsClass:
    x: int


wsc = WithSlotsClass(1)

wsc.y = 2  # AttributeError if slots is True


# is_dataclass
print(
    is_dataclass(wsc),
)


# functional style to make dataclass
FDC = make_dataclass('FuncDataclass', (('name', str), ('age', int, field(default=0))))

fdc = FDC('alex')

print(fdc)


# ClassVar
@dataclass
class WithClassVar:
    a: int
    counter: ClassVar[int] = 0

    def __post_init__(self):
        WithClassVar.counter += 1


wcv = WithClassVar(1)
wcv = WithClassVar(1)

print(WithClassVar.counter)
