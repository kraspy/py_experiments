from collections import namedtuple
from sys import getsizeof

# definition
NT = namedtuple('TupleName', ['field1', 'filed2'])

nt = NT('a', filed2='b')
print(nt)
print(nt[0], nt[1], nt.field1, nt.filed2)


# from iter
nt = NT._make(['f1', 'f2'])
print(nt)


# transform to dict
print(nt._asdict())


# new natedtuple with replace
nt1 = nt._replace(field1='...')
print(nt1)


# _fields (tuple of fields)
print(nt1._fields)


# defaults
ntd = namedtuple('Account', ['type', 'balance'], defaults=[0])
account = ntd('Deposit')
print(account)


# size
print(getsizeof(('Deposit', 0)))
print(getsizeof(account))


# exdended with properties
class Account(ntd):
    __slots__ = ()

    @property
    def get_info(self):
        print(self.type, self.balance)


ntc = Account(type='Depo')
ntc.get_info

print(ntc)
