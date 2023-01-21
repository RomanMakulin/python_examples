import view

def create_data(): # Создаем файл и записываем номера тлф
    with open('file.csv', 'w') as data:
        nums = '+7911111111 +792222222 +793333333 +79444444'
        data.write(nums)
        return nums

def data_coming(): # Получаем данные 
    with open('file.csv', 'r') as data:
        nums = data.read().split()
    return nums

def telephone_book(): # Формируем телефонный справочник
    return list(zip(view.i(), data_coming()))

def export_data(): # Заливаем справочник в файл
    with open('file_telephone_book.csv', 'a') as data:
        return data.write(str(f'\n{telephone_book()}'))



