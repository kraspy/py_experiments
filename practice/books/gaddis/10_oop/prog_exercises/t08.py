from t05 import RetailItem


class CashRegister:
    def __init__(self):
        self.__items = []

    def purchase_item(self, item: RetailItem):
        if not isinstance(item, RetailItem):
            raise TypeError('Можно добавить только объекты RetailItem.')
        self.__items.append(item)
        print(f'Добавлен товар: {item.description}')

    def get_total(self) -> float:
        return sum(
            [item.inventory * item.price for item in self.__items],
        )

    def show_items(self):
        if not self.__items:
            print('Список покупок пуст.')
            return

        print('\n--- Ваш список покупок ---')
        for i, item in enumerate(self.__items, 1):
            print(f'{i}. {item}')
        print('--------------------------')

    def clear(self):
        self.__items.clear()
        print('Список покупок очищен.')


if __name__ == '__main__':
    item1 = RetailItem('Куртка', 1, 59.99)
    item2 = RetailItem('Джинсы', 2, 34.50)
    item3 = RetailItem('Рубашка', 1, 25.00)
    item4 = RetailItem('Носки', 3, 5.99)

    available_items = {'1': item1, '2': item2, '3': item3, '4': item4}

    register = CashRegister()

    print('*** Добро пожаловать в магазин! ***')
    while True:
        print('\nДоступные товары:')
        for key, item in available_items.items():
            print(f'{key}. {item.description} (Цена: {item.price:.2f} руб.)')
        print('--------------------')
        print(
            'Введите номер товара для добавления в корзину (или "выход" для завершения):'
        )
        choice = input('> ').strip().lower()

        if choice in ('выход', 'exit'):
            break
        elif choice in available_items:
            register.purchase_item(available_items[choice])
        else:
            print('Неверный выбор. Введите номер товара из списка!')

    register.show_items()
    total_cost = register.get_total()
    print(f'Общая стоимость покупок: {total_cost:.2f} руб.')

    register.clear()
    register.show_items()
