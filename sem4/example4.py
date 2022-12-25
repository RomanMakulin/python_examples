# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 2
list = []
count = 0

while count < 4:
    list.append(f'{random.randint(0, 101)}')
    count += 1

with open('work2.txt', 'w') as data:
    data.write(f'{list[0]}x^{k} + {list[1]}x + {list[2]} = 0')