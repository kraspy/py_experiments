class RetailItem:
    def __init__(self, description: str, inventory: int, price: float):
        self.description = description
        self.inventory = inventory
        self.price = price

    def __str__(self):
        return f'{self.description}, {self.price}'


if __name__ == '__main__':
    item1 = RetailItem('Пиджак', 12, 59.95)
    item2 = RetailItem('Дизайнерские джинсы', 40, 34.95)
    item3 = RetailItem('Рубашка', 20, 24.95)

    print(
        f'Товар 1: {item1.description}, Количество: {item1.inventory}, Цена: {item1.price}'
    )
    print(
        f'Товар 2: {item2.description}, Количество: {item2.inventory}, Цена: {item2.price}'
    )
    print(
        f'Товар 3: {item3.description}, Количество: {item3.inventory}, Цена: {item3.price}'
    )
