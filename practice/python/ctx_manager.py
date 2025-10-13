from contextlib import contextmanager


class MyContextManager:
    def __init__(self, value: str) -> None:
        self._value = value

    def __enter__(self):
        print('Enter...')
        return self._value

    def __exit__(self, exc_type: str, exc_val: str, exc_tb: str):
        print(f'Exception Type: {exc_type}')
        print(f'Exception Value: {exc_val}')
        print(f'Exception Traceback: {exc_tb}')
        print('Exit...')
        return True


with MyContextManager('hi') as text:
    print(text.upper())
    print(1 / 0)


@contextmanager
def my_context(s: str):
    print('Enter...')
    yield s
    print('Exit...')


with my_context('hi') as text:
    print(text.capitalize())
