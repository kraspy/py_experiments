class BaseAccount:
    __slots__ = ('_username', '_email')

    __accounts_counter = 0

    @classmethod
    def _add_users_counter(cls):
        cls.__accounts_counter += 1

    @classmethod
    def get_total_accounts(cls):
        return f'Account counts: {cls.__accounts_counter}'

    def __repr__(self) -> str:
        attrs = ', '.join(
            f'{attr.lstrip("_")}={getattr(self, attr)!r}' for attr in self.__slots__
        )
        return f'{self.__class__.__name__}({attrs})'


class UserAccount(BaseAccount):
    __slots__ = ('_access_level', '_dynamic_attrs')

    def __init__(self, user_data: dict[str, str]) -> None:
        self._access_level: int | None = None
        self._dynamic_attrs = {}

        if not isinstance(user_data, dict):
            raise TypeError('❌ user_data must be a dict')

        for attr, value in user_data.items():
            if attr == 'username':
                self._username = value
            elif attr == 'email':
                self._email = value
            else:
                self._dynamic_attrs.update({attr: value})

        BaseAccount._add_users_counter()

    def __setattr__(self, attr, value) -> None:
        print(f'✅ Attr "{attr}" set/changed to "{value}"')
        return object.__setattr__(self, attr, value)

    def __getattribute__(self, attr) -> None:
        access_level = super().__getattribute__('_access_level')
        if (access_level is None) or (access_level < 1):
            if attr in super().__slots__:
                raise AttributeError('❌ Access Denied!')
        return super().__getattribute__(attr)

    def __delattr__(self, name: str) -> None:
        if name in BaseAccount.__slots__:
            raise ValueError(f'Attr "{name}" can\'t be deleted')
        return super().__delattr__(name)

    @property
    def profile(self):
        return {
            'username': self._username,
            'email': self._email,
        }

    @profile.setter
    def profile(self, user_data: dict[str, str]):
        if username := user_data.get('username'):
            self._username = username

        if email := user_data.get('email'):
            self._email = email


class AdminAccount(UserAccount):
    __slots__ = ()

    def __init__(self, user_data: dict[str, str]) -> None:
        super().__init__(user_data)
        self._access_level = 1


class GuestAccount(UserAccount):
    __slots__ = ()

    def __init__(self, user_data: dict[str, str]) -> None:
        super().__init__(user_data)
        self._access_level = 0


user_data = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'age': 25,
    'city': 'Moscow',
}

user = UserAccount(user_data)

print(user)


admin = AdminAccount({'username': 'admin', 'permissions': ['read', 'write', 'delete']})

print(admin)

try:
    print(hasattr(user, 'age'))
except AttributeError as e:
    print(e)
user.profile = {'bio': 'Software developer', 'interests': ['Python', 'ML']}

print(user)


print(getattr(admin, '_access_level'))

print(BaseAccount.get_total_accounts())
