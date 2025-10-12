def foo():
    raise Exception(f'Error from {foo.__name__}!')


def bar():
    foo()


try:
    bar()
except Exception as e:
    print(e)
else:
    print('Исключение не выбрасывалось')
finally:
    print('Выполнится в любом случае')


# Custom Exception
class MyException(BaseException):
    def __init__(self, message) -> None:
        self._message = message

    def __str__(self):
        return f'[Error]: {self._message}'


def throw_my_error():
    raise MyException('Тут ошибочка')


throw_my_error()
