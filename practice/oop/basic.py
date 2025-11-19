from abc import ABC, abstractmethod
from typing import Any, Protocol


# Abstract Class
class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def say(self, text):
        return text


# c = Animal('1')


# Mixins
class OneMixin:
    def method(self):
        print('method from OneMixin')


class TwoMixin:
    def method(self):
        print('method from TwoMinix')


class Class(OneMixin, TwoMixin):
    pass


c = Class()
print(Class.__mro__)
c.method()


# Duck typing
class Quackable(Protocol):
    def quack(self) -> None: ...


def make_sound(obj: Quackable):
    obj.quack()


class Duck:
    def quack(self):
        print('quack!')


make_sound(Duck())


# Context Manager
class CtxManager:
    def __init__(self) -> None:
        self.store = []

    def __enter__(self):
        print('Enter...')
        return self.store

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit...')
        self.store.clear()
        return False


with CtxManager() as cm:
    cm.append(1)
    print(cm)

print(cm)


# get, set, del
class TempClass:
    def __getattribute__(self, name: str) -> Any:
        print(f'__getattribute__: {name}')
        return super().__getattribute__(name)

    def __getattr__(self, name):
        print(f'__getattr__: {name}')
        return None

    def __setattr__(self, name: str, value: Any) -> None:
        print(f'__setattr__: {name}={value}')
        super().__setattr__(name, value)


tc = TempClass()
tc.a = 1

print(tc.a)
print(tc.b)


# Descriptors
class Descriptor:
    def __set_name__(self, owner, name):
        print(f'Set Name: _{name} ({owner.__name__})')
        return f'_{name}'

    def __get__(self, instance, owner):
        print(f'get: {instance=} / {owner=}')
        return instance._descriptor

    def __set__(self, instance, value):
        print(f'set: {instance=} / {value=}')
        instance._descriptor = value

    def __delete__(self, instance):
        print(f'del: {instance=}')
        del instance._descriptor


class MyClass:
    descriptor = Descriptor()


mc = MyClass()

mc.descriptor = 1

print(MyClass.__dict__, mc.__dict__, sep='\n\n')
print(mc.descriptor)
del mc.descriptor
