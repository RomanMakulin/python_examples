# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла)
# Исходите из уровня группы и студента.

# 1) list comprehension. Удалить слова, содержащие 'abc'
# string = 'Childrensabc are playing game. They are need to compare box an abc'.split()
# print(*[i for i in string if 'abc' not in i])

# 2) lambda, filter, map, zip. Сумма элементов на нечетных позициях
string = '1 1 2 4 8 9'.split()

new_result = list(filter((lambda i: i%2, range(len(string))), [i for i in string]))
print(*new_result)