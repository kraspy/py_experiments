class Person:
    def __init__(self, name: str, address: str, phone_num: str) -> None:
        self.name = name
        self.address = address
        self.phone_num = phone_num

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def phone_num(self):
        return self._phone_num

    @phone_num.setter
    def phone_num(self, phone_num: str):
        self._phone_num = phone_num

    def __str__(self):
        return f'Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_num}'


class Customer(Person):
    def __init__(
        self,
        name: str,
        address: str,
        phone_num: str,
        newsletter: bool = True,
    ) -> None:
        super().__init__(name, address, phone_num)
        self.newsletter = newsletter

    @property
    def newsletter(self):
        return self._newsletter

    @newsletter.setter
    def newsletter(self, newsletter: bool):
        self._newsletter = newsletter

    def __str__(self):
        return super().__str__() + f'\nNewsletter: {self.newsletter}'


customer1 = Customer('John Doe', 'Moscow, Kremlin', '+79998887766')

print(f'*** {customer1.__class__.__name__} ***\n{customer1}')
