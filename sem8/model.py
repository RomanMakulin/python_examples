def empty_string(): # Удаление пустых строк в файле
    with open('sem8/members.csv') as f:
        lines = f.readlines()
        non_empty_lines = (line for line in lines if not line.isspace())
        f.close
    with open('sem8/members.csv', 'w') as n_f:
        n_f.writelines(non_empty_lines)
        n_f.close

def find_person(key): # Нахождение человека из файла по ключу 
    empty_string()
    with open('sem8/members.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                print(f'First name: {first_name}, Second name: {second_name}, ID: {position}, Salary: {salary}, Doljnost: {doljnost}')
        file.close

def update_person(key): # Обновление данных 
    empty_string() # Удаляем пустые строки для чтения
    with open('sem8/members.csv', 'r') as file:
        data = file.read().split('\n')
        with open('sem8/members.csv', 'w') as file:
            for i in data:
                first_name, second_name, position, salary, doljnost = i.split(';')
                if position == key:
                    array = [first_name, second_name, position, salary, doljnost]
                    print(list(enumerate(array)))
                    n = int(input('Введите номер параметра, который хотите обновить: '))
                    array[n] = str(input('Введите обновленные данные: '))
                else:
                    with open('sem8/members.csv', 'a') as file:
                        file.write(f'\n{first_name};{second_name};{position};{salary};{doljnost}')
                        file.close
            with open('sem8/members.csv', 'a') as file:
                file.write(f'\n{";".join(array)}')
                file.close
            file.close
    empty_string() # Удаляем пустые строки после обновления параметров

def filter_doljnost(key): # Выборка по должности
    empty_string()
    with open('sem8/members.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            first_name, second_name, position, salary, doljnost = i.split(';')
            if doljnost == key:
                print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')
        file.close

def filter_salary(key): # Выборка по зарплате
    empty_string()
    with open('sem8/members.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            first_name, second_name, position, salary, doljnost = i.split(';')
            if salary == key:
                print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')
        file.close

def add_member(new):
    empty_string()
    first_name, second_name, position, salary, doljnost = new
    with open('sem8/members.csv', 'a') as file:
        member = f'\n{first_name};{second_name};{position};{salary};{doljnost}'
        file.write(member)
        file.close
    return 'New member was create'

def del_member(key):
    empty_string() # Удаляем пустые строки для чтения
    with open('sem8/members.csv', 'r') as file:
        data = file.read().split('\n')
        with open('sem8/members.csv', 'w') as file:
            for i in data:
                first_name, second_name, position, salary, doljnost = i.split(';')
                if position != key:
                    with open('sem8/members.csv', 'a') as file:
                        file.write(f'\n{first_name};{second_name};{position};{salary};{doljnost}')
                        file.close
            file.close
        file.close
    empty_string() # Удаляем пустые строки после обновления параметров

def export(key):
    with open('sem8/members.csv', 'r') as old_file:
        data = old_file.read()
        with open(key, 'w') as new_file:
            new_file.write(data)
            new_file.close
        old_file.close
    
def exit(key):
    return SystemExit()