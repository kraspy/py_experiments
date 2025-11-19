from abc import ABC, abstractmethod
from typing import Protocol


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
