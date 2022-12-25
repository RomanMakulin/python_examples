# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
final_list = []
reset_count = 1 # Переменная чтобы идти с конечного элемента списка
half_list = int(len(list) / 2) # Определение количества пар для перемножения (ограничение)
count = 0 # Счетчик необходимого количества пар

for i in list:
    if count < half_list:
        result = i * list[(len(list))-reset_count]
        final_list.append(result)
        reset_count += 1
        count += 1

print(f'Исходный список: {list}\nПеремножение пар списка: {final_list}')

# В данном задании я перемножаю пары чисел списка, не трогая одиночный элемент в середине
# Так как по условию, у него нет пары и это значение в нечетном количестве списка одно.