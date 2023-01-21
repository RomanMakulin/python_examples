import model

def import_view():
    print(f'Данные отправлены!')
    
def create_view():
    with open('file.txt', 'r') as data:
        print(f'Номера телефонов созданы\nФайл: "{data.name}"')

def data_coming_view(data):
    print(f'Телефоны получены: {data}')
    return data

def i():
    return [input(f'Введите имя для номера {i} : ') for i in model.data_coming()]
