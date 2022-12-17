# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
import random

list = [3, 2, 1, 6]
print(f'Исходный список: {list}')

for  i in range(len(list)-1, 0, -1):
    a = random.randint(0, i + 1)
    list[i], list[a] = list[a], list[i]
    
print(f'Перемешанный список: {list}')