from random import randint

right = 100000
left = 0
x = randint(left, right)

# counter_perebor = 0
#метод последовательного перебора
# for i in range(0,101):
#     counter_perebor += 1
#     if i == x:
#         print(f'Число найдено')
#         break
# print(f'Число найдено {x}. Итерации: {counter_perebor}')

# counter_random = 1
#метод случайного отгадывания
# y = randint(0, 100)
# while x != y:
#     y = randint(0, 100)
#     counter_random += 1

# print(f'Число найдено {x}. Итерации: {counter_random}')

# Бинарный метод поиска загаданного числа
count_bin = 1
print(f'Давай начнем игру - угадай число от {left} до {right}')
mid = (right + left) // 2

while x != mid:
    if x < mid: 
        right = mid - 1
    else: 
        left = mid + 1
    mid = (right + left) // 2
    count_bin += 1
print(f'Число найдено {x}. Итерации: {count_bin}')
