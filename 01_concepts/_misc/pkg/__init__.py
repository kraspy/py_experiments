# Импорт функций и классов из модулей пакета
from .module1 import MyClass1, function1, function2
from .module2 import MyClass2, function3

print('Пакет my_package инициализирован')

__all__ = ['MyClass1', 'MyClass2', 'function1', 'function2', 'function3']
