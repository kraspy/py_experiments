from datetime import datetime as dt


class PasswordField:
    def __get__(self, instance, owner):
        print(f'📤 PasswordField [__get__]: {instance=}, {owner=}')
        return '*****'

    def __set__(self, instance, value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError('❌ Пароль должен быть строкой минимум из 8 символов')

        print(f'📥 PsswordField [__set__]: {instance=}, {value=}')
        instance._password = hash(value)

    def __delete__(self, instance):
        pass
        # print(f'PsswordField [__sel__]: {instance=}, {owner=}')
        # ...


class EmailField:
    def __get__(self, instance, owner):
        print(f'📤 EmailField [__get__]: {instance=}, {owner=}')
        return instance._email

    def __set__(self, instance, value):
        if (
            not isinstance(value, str)
            or '@' not in value
            or '.' not in value.split('@')[-1]
        ):
            raise ValueError('❌ Адрес email должен содержать символ "@"')

        print(f'📥 EmailField [__set__]: {instance=}, {value=}')
        instance._email = value.lower()


class MetadataField:
    def __init__(self) -> None:
        self.counter = 0
        self.created_at = dt.utcnow()

    def __get__(self, instance, owner):
        print(f'📤 MetadataField [__get__]: {instance=}, {owner=}')

        if instance is None:
            return self

        self.counter += 1

        return {
            'created_at': self.created_at,
            'requests': self.counter,
        }


class UserAccount:
    password = PasswordField()
    email = EmailField()
    metadata = MetadataField()


acc = UserAccount()

# Установка значений
acc.email = 'User@mail.ru'
acc.password = '12345678'

print('\n=== Чтение значений ===')
print(f'{acc.email=}')
print(f'{acc.password=}')
print(f'{acc.metadata=}')
for i in range(10_000):
    i**i
print(f'{acc.metadata=}')

print('\n=== Приоритет ===')
acc.email = 'admin@mail.ru'
acc.__dict__['email'] = 'EMAIL'

print(acc.email)
