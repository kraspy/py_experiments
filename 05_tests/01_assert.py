# assert игнорируется, если запустить `python -O`
# if __debug__:
#     if not <условие>:
#         raise AssertionError(<сообщение>)

assert 1 + 1 == 2, 'Ошибка: 1 + 1 не равно 2'


# Тест функций
def foo(x):
    return x


assert foo(1) == foo(2), 'Ошибка: foo() не равно bar()'
