
def find_person(key): # Нахождение человека из файла по ключу 
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                return print(f'{first_name} {second_name}, {position}, {salary}, {doljnost}')
            else:
                return print('Not found')

def update_person(key):

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
                        file.write(f'\n{first_name} {second_name}, {position}, {salary}, {doljnost}')
            with open('sem8/phonebook.csv', 'a') as file:
                a = ', '
                file.write(f'\n{a.join(array)}')

    with open('sem8/phonebook.csv', 'r') as data:
        for i in data:
            if i.strip():
                data.write(i)

update_person('Makulin')

def filter_doljnost():
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        need_category = []
        for i in data:
            first_name, second_name, position, salary, doljnost = i.split(';')
            need_category.append(doljnost)
        return print(need_category)

def filter_salary():
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        need_category = []
        for i in data:
            first_name, second_name, position, salary, doljnost = i.split(';')
            need_category.append(salary)
        return print(need_category)

def add_member(new):
    first_name, second_name, position, salary, doljnost = new
    with open('sem8/phonebook.csv', 'a') as file:
        member = f'\n{first_name};{second_name};{position};{salary};{doljnost}'
        file.write(member)
    return 'New member was create'
        
            


