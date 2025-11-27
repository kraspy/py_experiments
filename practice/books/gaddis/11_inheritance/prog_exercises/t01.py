from enum import Enum


class Employee:
    def __init__(self, name: str, id_num: int) -> None:
        self.name = name
        self.id_num = id_num

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def id_num(self):
        return self._id_num

    @id_num.setter
    def id_num(self, id_num: int):
        self._id_num = id_num

    def __str__(self):
        return f'Name: {self.name}\nID: {self.id_num}'


class Shift(Enum):
    DAY = 1
    NIGHT = 2


class ProductionWorker(Employee):
    def __init__(
        self,
        name: str,
        id_num: int,
        shift: Shift,
        hourly_pay_rate: float,
    ) -> None:
        super().__init__(name, id_num)
        self.shift = shift
        self.hourly_pay_rate = hourly_pay_rate

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, shift: Shift):
        self._shift = shift

    @property
    def hourly_pay_rate(self):
        return self._hourly_pay_rate

    @hourly_pay_rate.setter
    def hourly_pay_rate(self, hourly_pay_rate: float):
        self._hourly_pay_rate = hourly_pay_rate

    def __str__(self):
        return (
            f'{super().__str__()}'
            f'\nShift: {self.shift.name}'
            f'\nHourly Pay Rate: {self.hourly_pay_rate}'
        )


def main():
    worker1 = ProductionWorker('John Doe', 12345, Shift.DAY, 15.50)
    worker1.hourly_pay_rate = 20

    print(worker1)


if __name__ == '__main__':
    main()
