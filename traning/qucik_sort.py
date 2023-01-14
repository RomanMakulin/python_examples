# Сортировка Quick Sort. 
# Одна из лучших сортировок. Делается через рекурсию
# Ключевые слова: лево, право, центр
import random

array = [i for i in range(1, 30)]
random.shuffle(array)
array = array[:10]
print(array)

def quick_sort(array):
    if len(array) <= 1:
        return array
    element = array[0]

    left = list(filter(lambda i: i < element, array))
    center = [i for i in array if i == element]
    right = list(filter(lambda i: i > element, array))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort(array))
