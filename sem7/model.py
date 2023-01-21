def create_data(): # Создаем данные
    with open('file.txt', 'w') as data:
        nums = '+791600252 +743242321 +794328421 +792131234'
        data.write(nums)
        return nums

def data_coming(): # Получаем данные 
    with open('file.txt', 'r') as data:
        nums = data.read().split()
        return nums
 
def telephone_book():
    names = 'Roman Olga Igor Fedor Kristina Oleg Alexander'.split()
    new_book = list(zip(names, data_coming()))
    return new_book

def import_data():
    with open('file.txt', 'a') as data:
        return data.write(str(f'\n{telephone_book()}'))