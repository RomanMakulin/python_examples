# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла)
# Исходите из уровня группы и студента.

#  -----------------------------------------

# 1) Удаляем ненужные символы из текста задания, вводим номера вариантов, выбираем четные
# и присваем каждому студенту + выбрать уровень сложности

# task = 'Даны три нужныхabc списка. Определить abc номер варианта (четный) и уровень сложности для каждого студента.'.split()
# print(*[i for i in task if 'abc' not in i])

# string = map(int, '1 1 2 4 8 9 10'.split()) # map используем ввод с преобразованием строки в int
# names = 'Roman, Olga, Ann, Max'.split()
# hardest = 'middle+, low+, hard+, hard'.split()

# new_result = list(filter(lambda i: not i%2, string)) # фильтрация четных элементов filter
# print(*zip(new_result, names, hardest)) # Используем zip для определения варианта

#  -----------------------------------------

# 2) Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# string = list(map(int, '1 2 1 4 5 1 4'.split())) # 1 2 4 5
# nums = []; [nums.append(i) for i in string if i not in nums]
# print(nums)
# print('-'*30)

#  -----------------------------------------

# # 3) -n до n
# a = 4
# b = [i for i in range(-a,a+1)]
# print(b)
# print('-'*30)

#  -----------------------------------------

# # 4) нечетные позиции
# c = list(map(int, '1 24 5 1 2 6'.split()))
# print([c[i] for i in range(0, len(c), 2)]),

#  -----------------------------------------

# 5) enumerate. сложение под четными индексами
# list = [2, 4, 1, 8, 9, 10]
# new_list = [nums for i, nums in enumerate(list) if i%2 == 0]
# print(new_list)

# from functools import reduce
# sum_all = reduce(lambda x,y: x + y, new_list)
# print (sum_all)





