# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка .
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('X: '))
y = int(input('Y: '))

def check_quarter(x,y):
    quarter = ''
    if x == 0 and x == 0:
        print('Введите значения отличные от нуля')
        return
    if x > 0 and y > 0:
        quarter = 'I'
    if x < 0 and y > 0:
        quarter = 'II'
    if x < 0 and y < 0:
        quarter = 'III'
    if x > 0 and y < 0:
        quarter = 'IV'
    print(f'Точка с координатами XY[{x},{y}] находится в {quarter} четверти')

check_quarter(x, y)