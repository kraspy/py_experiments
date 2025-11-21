from enum import StrEnum


class AnimalType(StrEnum):
    CAT = 'кот'
    DOG = 'собака'
    BIRD = 'птица'


class Pet:
    def __init__(self, name: str, type: AnimalType, age: int) -> None:
        self.__name = name
        self.__anymal_type = type
        self.__age = age

    def set_name(self, value: str) -> None:
        self.__name = value

    def set_animal_type(self, value: AnimalType) -> None:
        self.__anymal_type = value

    def set_age(self, value: int) -> None:
        self.__age = value

    def get_name(self) -> str:
        return self.__name

    def get_animal_type(self) -> str:
        return self.__anymal_type

    def get_age(self) -> str:
        return self.__age

    def __str__(self) -> str:
        return (
            f'Вид: {self.__anymal_type.value.capitalize()}\n'
            f'Имя: {self.__name}\n'
            f'Возраст: {self.__age}'
        )


animal = Pet(
    input('Введите имя питомца: '),
    AnimalType(
        input(f'Введите тип питомца ({[", ".join(a.value for a in AnimalType)]}): ')
    ),
    input('Введите возраст питомца: '),
)

print(animal)
