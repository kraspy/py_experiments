class Car:
    def __init__(
        self,
        year_model: int,
        make: str,
        speed: int,
    ) -> None:
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self) -> None:
        self.__speed += 5

    def brake(self) -> None:
        self.__speed -= 5

    def get_speed(self) -> int:
        return self.__speed


def main():
    my_car = Car(2025, 'Tesla', 0)

    print('Ускорение автомобиля:')
    for _ in range(5):
        my_car.accelerate()
        print(f'Текущая скорость: {my_car.get_speed()} км/ч')

    print('\nТорможение автомобиля:')
    for _ in range(5):
        my_car.brake()
        print(f'Текущая скорость: {my_car.get_speed()} км/ч')


if __name__ == '__main__':
    main()
