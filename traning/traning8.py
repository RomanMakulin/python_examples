# Вводится списое целых чисел в одну строку через пробел
# Необходимо оставить только двузначные числа
# использовать filter

# string = list(map(int, input().split()))
# print(list(filter((lambda i: 10 <= abs(i) <= 100), string)))
# print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))

# Дан список, вывести отдельно буквы и цифры
# a = ('a', 'b', '2')

# a = ('a', 'b', '22', 'c')
# b = filter(str.isalpha, a)
# c = filter(str.isdigit, a)

# print(*b)
# print(*c)

items = '/calc 1 2 4 1'.split()

for i in items:
    if i.isdigit():
        result = result + int(i)
print(result)


