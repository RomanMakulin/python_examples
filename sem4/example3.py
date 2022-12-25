#  Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = [1, 2, 1, 4, 5, 1, 4] # 1 2 4 5
result_list = []

for i in list:
    if i not in result_list:
        result_list.append(i)
        
# result_list = set(list)

print(result_list)

