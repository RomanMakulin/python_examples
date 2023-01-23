
def find_person(key): # Нахождение человека из файла по ключу 
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary = i.split(';')
                table = 'Name Pos Salary'.split()
                values = [f'{first_name} {second_name}', position, salary]
                result = zip(table, values)
                
                return print(*result)
            else:
                return print('Not found')

def update_person(key):
    with open('sem8/phonebook.csv', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if i.count(key):
                first_name, second_name, position, salary, doljnost = i.split(';')
                table = 'Name Pos Salary Doljnost'.split()
                values = [f'{first_name} {second_name}', position, salary, doljnost]
                table.append(input('Введите категорию: '))
                values.append(input('Введите значение: '))
                result = zip(table, values)
                
                return print(*result)
            else:
                return print('Not found')
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
        
            


