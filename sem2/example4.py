# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

n = 2
array = list(range(-n, n+1))
number_pos = [3, 1]
result = array[number_pos[0]] * array[number_pos[1]]
print(f'Список элементов N({n}): {array}\nРезультат перемножений позиций {number_pos} = {result}')