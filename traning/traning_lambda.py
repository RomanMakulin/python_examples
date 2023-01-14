# Изучили функции map filter zip and another lambda

import random
# Создание массива
array = [i for i in range(1, 100)]
random.shuffle(array)
array = array[:10]
print(array)

# Фильтрация массива по четным/не четным
array = list(filter(lambda i: not i%2, array))
print(array)

# Изменение элементов массива (+10 к каждому)
array = list(map(lambda i:i + 10, array))
print(array)

# Добавление айди с помощью ZIP
ids = ['a', 'b', 'c']
array = list(zip(ids, array))

print(array)

