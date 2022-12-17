# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = 4
count = 0
result = 1
array = []

while count < n:
    count += 1
    result *= count
    array.append(result)

print(array)