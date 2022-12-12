# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import cmath

a = []
b = []

def input_coordinate(a):
    x = int(input("X: "))
    y = int(input("Y: "))
    return [x, y]

a = input_coordinate(a)
print(f'A: {a}')
b = input_coordinate(b)
print(f'B: {b}')

def check(a, b):
    import math
    result = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    return result

print(check(a, b))
