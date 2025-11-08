import enum


# Simple creation
class MyEnum(enum.Enum):
    VALUE1 = 1
    ALIAS_VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3


# Get Values
print(
    MyEnum(1),
    MyEnum['VALUE1'],
    MyEnum.VALUE1,
    sep='\n',
)


# Members
print(MyEnum.__members__)


# Iteration by members
for member in MyEnum:
    print(f'{member.name=} => {member.value=}')


# Aliases
v = MyEnum.VALUE1
av = MyEnum.ALIAS_VALUE1

print(f'{v is av=}')
