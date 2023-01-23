import view

def create_data(): # Создаем файл и записываем номера тлф
    with open('file.txt', 'w') as data:
        nums = '+79686164588 +79859755371'
        data.write(nums)
        return nums

def data_coming(): # Получаем данные 
    with open('file.txt', 'r') as data:
        nums = data.read().split()
    return nums

def telephone_book(): # Формируем телефонный справочник
    return list(zip(view.i(), data_coming()))

def export_data(): # Заливаем справочник в файл
    with open('file_telephone_book.txt', 'a') as data:
        return data.write(str(f'\n{telephone_book()}'))



