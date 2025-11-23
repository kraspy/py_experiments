class Employee:
    def __init__(self, name: str, employee_id: str, department: str, job_title: str):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Идентификационный номер: {self.employee_id}\n'
            f'Отдел: {self.department}\n'
            f'Должность: {self.job_title}'
        )


if __name__ == '__main__':
    employee1 = Employee('Сьюзан Мейерс', '47899', 'Бухгалтерия', 'Вице-президент')
    employee2 = Employee('Марк Джоунс', '39119', 'IT', 'Программист')
    employee3 = Employee('Джой Роджерс', '81774', 'Производственный', 'Инженер')

    print('Данные сотрудника 1:')
    print(employee1)
    print('\nДанные сотрудника 2:')
    print(employee2)
    print('\nДанные сотрудника 3:')
    print(employee3)
