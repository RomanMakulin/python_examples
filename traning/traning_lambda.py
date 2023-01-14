# Изучили функции map filter zip and another lambda
# Создание массива
array = [i for i in range(1, 11)]
print(array)

array = list(filter(lambda i: not i%2, array))
print(array)

array = list(map(lambda i:i + 10, array))
print(array)

ids = ['a', 'b', 'c']

array = list(zip(ids, array))

print(array)