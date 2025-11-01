class PhoneConverter:
    NUMBER_PARTS = 3
    AL_NUM_ASSOCIATIONS = {
        'A': 2, 'B': 2, 'C': 2,
        'D': 3, 'E': 3, 'F': 3,
        'G': 4, 'H': 4, 'I': 4,
        'J': 5, 'K': 5, 'L': 5,
        'M': 6, 'N': 6, 'O': 6,
        'P': 7, 'Q': 7, 'R': 7, 'S': 7,
        'T': 8, 'U': 8, 'V': 8,
        'W': 9, 'X': 9, 'Y': 9, 'Z': 9,
    }  # fmt: skip

    def __init__(self, phone_number) -> None:
        self.check_phone_number(phone_number)
        self.phone_number = phone_number

    @classmethod
    def check_phone_number(cls, phone_number: str) -> bool:
        """Проверка номера на соответствие формату XXX-XXX-XXXX"""
        if not isinstance(phone_number, str):
            raise ValueError('Телефонный номер должен быть строкой')
        if splitted_phone_number := phone_number.split('-'):
            if len(splitted_phone_number) != cls.NUMBER_PARTS:
                raise ValueError(
                    'Телефонный номер должен быть в формате "XXX-XXX-XXXX"'
                )
        if not all(part.isalnum() for part in splitted_phone_number):
            raise ValueError(
                'Телефонный номер должен состоять из латинских букв, цифр и знака -'
            )

        return True

    @classmethod
    def change_al_to_num(cls, char: str) -> str:
        """Преобразует буквы в цифры"""
        if char == '-':
            return char
        return char if char.isdigit() else str(cls.AL_NUM_ASSOCIATIONS[char.upper()])

    def convert(self) -> str:
        """Конвертирует строку вида XXX-XXX-XXXX в номер телефона"""
        converted_number_array = []

        for char in self.phone_number:
            converted_number_array.append(self.change_al_to_num(char))

        return ''.join(converted_number_array)


def main():
    user_input = input('Введите номер телефона в формате "XXX-XXX-XXXX": ')
    converter = PhoneConverter(user_input)

    result = converter.convert()

    print(result)


if __name__ == '__main__':
    main()
