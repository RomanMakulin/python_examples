# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
size = 100 # Кол-во конфет
limit = 28 # Максимальное кол-во конфет которое можно забрать
a_count = 0 # Кол-во конфет первого игрока
b_count = 0 # Кол-во конфет второго игрока   

while size > 0:
    second = int(input('Roman Введите какое кол-во конфет забираете: '))
    if size >= second and second <= limit:
        size = size - second
        b_count += second
    else:
        print('Что-то пошло не так, пропуск хода')
    print(f'Roman забрал {second} конфет')
    print(f'Конфет у Roman: {b_count}')
    print(f'Конфет осталось: {size}')
    print()

    first = random.randint(1,limit + 1)
    if size >= first and first <= limit:
        size = size - first
        a_count += first
    else:
        print('Что-то пошло не так, пропуск хода')
    print(f'Maxim забрал {first} конфет')
    print(f'Конфет у Maxin: {a_count}')
    print(f'Конфет осталось: {size}')
    print()

print('Игра закончена')
print(f'Общий счет: Roman ({b_count}), Maxim({a_count})')

# from random import randint

# a = int(input('Введите количество конфет'))
# hod = 0
# wins = {0: 'Игрок', 1: 'Бот'}
# while a > 0:
#     if a <= 28:
#         print(f'Выиграл {wins[hod]}')
#         break
#     if hod % 2 == 0:
#         print('Ход Игрока')
#         d = int(input('Введите количество конфет, которое хотите взять'))
#         a -= d
#         print(f'Осталось конфет: {a}')
#     else:
#         print('Ход Бота')
#         d = a % 29
#         a -= d
#         print(f'Осталось конфет: {a}')
#     hod = (hod + 1) % 2
