from t01 import Employee


class ShiftSupervisor(Employee):
    def __init__(
        self, name: str, id_num: int, annual_salary: float, annual_bonus: float
    ) -> None:
        super().__init__(name, id_num)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

    @property
    def annual_salary(self):
        return self._annual_salary

    @annual_salary.setter
    def annual_salary(self, annual_salary: float):
        self._annual_salary = annual_salary

    @property
    def annual_bonus(self):
        return self._annual_bonus

    @annual_bonus.setter
    def annual_bonus(self, annual_bonus: float):
        self._annual_bonus = annual_bonus

    def __str__(self):
        return (
            f'{super().__str__()}'
            f'\nAnnual Salary: {self.annual_salary}'
            f'\nAnnual Bonus: {self.annual_bonus}'
        )


supervisor1 = ShiftSupervisor('John Doe', 12345, 50000, 10000)
print(supervisor1)
