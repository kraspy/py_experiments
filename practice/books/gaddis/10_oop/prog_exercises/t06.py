class Patient:
    def __init__(
        self,
        first_name: str,
        middle_name: str,
        last_name: str,
        address: str,
        city: str,
        state: str,
        post_code: str,
        phone_number: str,
        emergency_contact_name: str,
        emergency_contact_phone: str,
    ):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._address = address
        self._city = city
        self._state = state
        self._post_code = post_code
        self._phone_number = phone_number
        self._emergency_contact_name = emergency_contact_name
        self._emergency_contact_phone = emergency_contact_phone

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = value

    @property
    def middle_name(self) -> str:
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value: str):
        self._middle_name = value

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        self._last_name = value

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, value: str):
        self._address = value

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str):
        self._state = value

    @property
    def post_code(self) -> str:
        return self._post_code

    @post_code.setter
    def post_code(self, value: str):
        self._post_code = value

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        self._phone_number = value

    @property
    def emergency_contact_name(self) -> str:
        return self._emergency_contact_name

    @emergency_contact_name.setter
    def emergency_contact_name(self, value: str):
        self._emergency_contact_name = value

    @property
    def emergency_contact_phone(self) -> str:
        return self._emergency_contact_phone

    @emergency_contact_phone.setter
    def emergency_contact_phone(self, value: str):
        self._emergency_contact_phone = value

    def __str__(self) -> str:
        return (
            f'Информация о пациенте:\n'
            f'  ФИО: {self.last_name} {self.first_name} {self.middle_name}\n'
            f'  Адрес: {self.address}, {self.city}, {self.state}, {self.post_code}\n'
            f'  Телефон: {self.phone_number}\n'
            f'  Экстренный контакт: {self.emergency_contact_name}, {self.emergency_contact_phone}'
        )


class Procedure:
    """
    Представляет медицинскую процедуру, пройденную пациентом.
    """

    def __init__(
        self,
        procedure_name: str,
        procedure_date: str,
        doctor_name: str,
        procedure_cost: float,
    ):
        self._procedure_name = procedure_name
        self._procedure_date = procedure_date
        self._doctor_name = doctor_name
        self._procedure_cost = procedure_cost

    @property
    def procedure_name(self) -> str:
        return self._procedure_name

    @procedure_name.setter
    def procedure_name(self, value: str):
        self._procedure_name = value

    @property
    def procedure_date(self) -> str:
        return self._procedure_date

    @procedure_date.setter
    def procedure_date(self, value: str):
        self._procedure_date = value

    @property
    def doctor_name(self) -> str:
        return self._doctor_name

    @doctor_name.setter
    def doctor_name(self, value: str):
        self._doctor_name = value

    @property
    def procedure_cost(self) -> float:
        return self._procedure_cost

    @procedure_cost.setter
    def procedure_cost(self, value: float):
        self._procedure_cost = value

    def __str__(self) -> str:
        return (
            f'  Название процедуры: {self.procedure_name}\n'
            f'  Дата: {self.procedure_date}\n'
            f'  Врач: {self.doctor_name}\n'
            f'  Стоимость: {self.procedure_cost:.2f} руб.'
        )


if __name__ == '__main__':
    patient = Patient(
        first_name='Иван',
        middle_name='Иванович',
        last_name='Иванов',
        address='ул. Мира, д. 1',
        city='Красноярск',
        state='Красноярский край',
        post_code='660000',
        phone_number='+79998887766',
        emergency_contact_name='Елена Иванова',
        emergency_contact_phone='+78887776655',
    )

    today_date = 'сегодняшняя'
    procedure1 = Procedure('врачебный осмотр', today_date, 'Ирвин', 250.00)
    procedure2 = Procedure('рентгенография', today_date, 'Джемисон', 500.00)
    procedure3 = Procedure('анализ крови', today_date, 'Смит', 200.00)
    print(patient)
    print('\n--- Сведения о процедурах ---')

    procedures = [procedure1, procedure2, procedure3]
    total_cost = 0.0

    for i, proc in enumerate(procedures):
        print(f'\nПроцедура №{i + 1}:')
        print(proc)
        total_cost += proc.procedure_cost

    print(f'\nКоличество процедур: {len(procedures)}')
    print(f'\nОбщая стоимость всех процедур: {total_cost:.2f} руб.')
