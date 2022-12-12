# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))

def check_xy(number):
    if number == 1:
        x = 1
        y = 1
        print(f'Возмождный диапозон координат XY в {number} четверти:\nX: От 1 до 99 \t Y: От 1 до 99\nПример:')
        for i in range(10):
            print(f'XY[{x}, {y}]')
            y += 1
    if number == 2:
        x = 1
        y = 1
        print(f'Возмождный диапозон координат XY в {number} четверти: \nX: От -99 до -1 \tY: От 1 до 99')
        for i in range(10):
            print(f'XY[{-x}, {y}]')
            y += 1
    if number == 3:
        x = 1
        y = 1
        print(f'Возмождный диапозон координат XY в {number} четверти: \nX: От -99 до -1 \tY: От -99 до -1')
        for i in range(10):
            print(f'XY[{-x}, {-y}]')
            y += 1
    if number == 4:
        x = 1
        y = 1
        print(f'Возмождный диапозон координат XY в {number} четверти: \nX: От 1 до 99 \tY: От -99 до -1')
        for i in range(10):
            print(f'XY[{x}, {-y}]')
            y += 1

check_xy(number)