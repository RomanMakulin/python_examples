# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [5, 2, 1, 5, 5, 1]
# sum = 0
# count = 0
#
# for i in list:
#     if count % 2 != 0:
#         sum += i
#     count += 1
# print(f'Исходный список: {list}\nСумма элементов на нечетной позиции = {sum}')

list = [5, 2, 1, 5, 5, 1, 1, 1]
sum = 0

for i in range(1,len(list),2):
    sum += list[i]
print(f'Исходный список: {list}\nСумма элементов на нечетной позиции = {sum}')