
def show_menu():
    print("\n" + "=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Найти сотрудника: ")
    print("2. Сделать выборку сотрудников по должности: ")
    print("3. Сделать выборку сотрудников по зарплате: ")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))

def find():
    return input('Введите ключевое слово для поиска сотрудника: ')

def upd():
    return input('Введите ID пользователя для обновления параметра: ')

def delete():
    return input('Введите ID пользователя для удаления: ')

def doljnost():
    return input('Введите должность для получения списка сотрудников: ')

def salary():
    return input('Введите ЗП для получения списка сотрудников: ')

def add_new_personal():
    name = input('Name: ')
    surname = input('Surname: ')
    position = input('Position: ')
    salary = input('Salary: ')
    doljnost = input('Doljnost: ')
    return name, surname, position, salary, doljnost

def info(message):
    print('Done')

def exporting():
    return input('Введите название файла с нужным форматом: ')

def prog_out():
    return print('Finishing programm')