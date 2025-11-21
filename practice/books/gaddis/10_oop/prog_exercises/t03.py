class Information:
    def __init__(self, name: str, address: str, age: int, phone_number: str):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_address(self) -> str:
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError('Возраст не может быть отрицательным.')

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def __str__(self):
        return (
            f'Имя: {self.__name}, Адрес: {self.__address}, '
            f'Возраст: {self.__age}, Телефон: {self.__phone_number}'
        )


my_info = Information('Evgeniy', 'Krasnoyarsk', 30, '+79998887766')

friend1_info = Information('Max', 'Moscow', 30, '+78887776655')
friend2_info = Information('Julia', 'St. Petersburg', 30, '+77776665544')

if __name__ == '__main__':
    print('Информация обо мне:')
    print(my_info)

    print('\nИнформация о друге 1:')
    print(friend1_info)

    print('\nИнформация о друге 2:')
    print(friend2_info)
