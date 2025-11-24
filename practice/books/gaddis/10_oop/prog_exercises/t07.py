import pickle
import os

from t04 import Employee

FILENAME = 'employees.dat'


def load_employees(filename):
    """Загружает словарь сотрудников из файла."""
    employees = {}
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as f:
                employees = pickle.load(f)
            print('Данные сотрудников успешно загружены.')
        except (EOFError, pickle.UnpicklingError):
            print(f'Файл {filename} поврежден или пуст. Создан новый пустой словарь.')
            employees = {}
        except Exception as e:
            print(
                f'Произошла ошибка при загрузке данных: {e}. Создан новый пустой словарь.'
            )
            employees = {}
    else:
        print('Файл данных не найден. Создан новый пустой словарь.')
    return employees


def save_employees(filename, employees_dict):
    """Сохраняет словарь сотрудников в файл."""
    try:
        with open(filename, 'wb') as f:
            pickle.dump(employees_dict, f)
        print('Данные сотрудников сохранены.')
    except Exception as e:
        print(f'Ошибка при сохранении данных: {e}')


def display_menu():
    """Выводит меню программы."""
    print('\n--- Система управления персоналом ---')
    print('1. Найти сотрудника')
    print('2. Добавить нового сотрудника')
    print('3. Изменить данные сотрудника')
    print('4. Удалить сотрудника')
    print('5. Выйти')


def find_employee(employees_dict):
    """Ищет и выводит информацию о сотруднике по ID."""
    id_num = input('Введите ID сотрудника для поиска: ')
    employee = employees_dict.get(id_num)
    if employee:
        print('\nНайден сотрудник:')
        print(employee)
    else:
        print('Сотрудник с таким ID не найден.')


def add_employee(employees_dict):
    """Добавляет нового сотрудника в словарь."""
    id_num = input('Введите ID нового сотрудника: ')
    if id_num in employees_dict:
        print('Сотрудник с таким ID уже существует.')
        return

    name = input('Введите имя сотрудника: ')
    department = input('Введите отдел сотрудника: ')
    job_title = input('Введите должность сотрудника: ')

    new_employee = Employee(id_num, name, department, job_title)
    employees_dict[id_num] = new_employee
    print('Сотрудник успешно добавлен.')


def modify_employee(employees_dict):
    """Изменяет данные существующего сотрудника."""
    id_num = input('Введите ID сотрудника для изменения: ')
    employee = employees_dict.get(id_num)
    if employee:
        print('\nТекущие данные сотрудника:')
        print(employee)
        print('\nВведите новые данные (оставьте пустым, чтобы не менять):')

        new_name = input(f'Новое имя ({employee.get_name()}): ')
        if new_name:
            employee.set_name(new_name)

        new_department = input(f'Новый отдел ({employee.get_department()}): ')
        if new_department:
            employee.set_department(new_department)

        new_job_title = input(f'Новая должность ({employee.get_job_title()}): ')
        if new_job_title:
            employee.set_job_title(new_job_title)

        print('Данные сотрудника успешно обновлены.')
    else:
        print('Сотрудник с таким ID не найден.')


def delete_employee(employees_dict):
    """Удаляет сотрудника из словаря."""
    id_num = input('Введите ID сотрудника для удаления: ')
    if id_num in employees_dict:
        del employees_dict[id_num]
        print('Сотрудник успешно удален.')
    else:
        print('Сотрудник с таким ID не найден.')


def main():
    """Основная функция программы."""
    employees = load_employees(FILENAME)

    while True:
        display_menu()
        choice = input('Выберите пункт меню: ')

        if choice == '1':
            find_employee(employees)
        elif choice == '2':
            add_employee(employees)
        elif choice == '3':
            modify_employee(employees)
        elif choice == '4':
            delete_employee(employees)
        elif choice == '5':
            save_employees(FILENAME, employees)
            print('Выход из программы.')
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте снова.')


if __name__ == '__main__':
    main()
