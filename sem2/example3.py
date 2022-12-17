# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = 6
list = []
count = 0
result = 0

for i in range(n):
    count += 1
    a = round(((1+1/count)**count), 3)
    list.append(a)
    result += a

print(f'Последовательность: {list}\nСумма: {round(result, 2)}')
