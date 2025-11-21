class BankAccount:
    def __init__(
        self,
        init_balance: int,
        interest: int,
    ) -> None:
        self.__amount = init_balance
        self.__interest = interest

    def deposit_money(self, amount: float) -> None:
        self.__amount += amount

    def withdraw_money(self, amount: float) -> None:
        self.__amount -= amount

    def get_interesst_profit(self) -> None:
        self.__amount += self.__amount * self.__interest / 100

    def __str__(self):
        return f'Money: {self.__amount:.2f}'


ba = BankAccount(1000, 10)
print(ba)

ba.deposit_money(100)
print(ba)

ba.get_interesst_profit()
print(ba)
