def empty_string(): # Удаление пустых строк в файле
    with open('sem8/phonebook.csv') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())

    with open('sem8/phonebook.csv', 'w') as n_f:
        n_f.writelines(non_empty_lines)

def find_person(key): # Нахождение человека из файла по ключу 
    empty_string()
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')


def update_person(key): # Обновление данных 
    empty_string() # Удаляем пустые строки для чтения
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        with open('sem8/phonebook.csv', 'w') as file:
            for i in data:
                if i.count(key):
                    first_name, second_name, position, salary, doljnost = i.split(';')
                    array = [first_name, second_name, position, salary, doljnost]
                    n = int(input('Введите номер параметра, который хотите обновить: '))
                    array[n] = str(input('Введите обновленные данные: '))
                else:
                    first_name, second_name, position, salary, doljnost = i.split(';')
                    with open('sem8/phonebook.csv', 'a') as file:
                        file.write(f'\n{first_name};{second_name};{position};{salary};{doljnost}')
            with open('sem8/phonebook.csv', 'a') as file:
                a = ';'
                file.write(f'\n{a.join(array)}')
    empty_string() # Удаляем пустые строки после обновления параметров

def filter_doljnost(key): # Выборка по должности
    empty_string()
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')


def filter_salary(key): # Выборка по зарплате
    empty_string()
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                if salary == key:
                    print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')

def add_member(new):
    empty_string()
    first_name, second_name, position, salary, doljnost = new
    with open('sem8/phonebook.csv', 'a') as file:
        member = f'\n{first_name} {second_name}, {position}, {salary}, {doljnost}'
        file.write(member)
    return 'New member was create'
        
            


