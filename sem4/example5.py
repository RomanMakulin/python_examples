# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

array = []
array2 = []
new_arr = []
new_arr2 = []

with open('work1.txt') as file:
    for line in file:
        array = line.split()

with open('work2.txt') as file:
    for line in file:
        array2 = line.split()

for i in array:
    if i != '+' and i != '=' and i != '0': 
        new_arr.append(i)

for i in array2:
    if i != '+' and i != '=' and i != '0': 
        new_arr2.append(i)

print(new_arr)
print(new_arr2)

with open('result.txt', 'w') as data:
    data.write(f'Funks:\n')
    data.write(f'{new_arr}\n')
    data.write(f'{new_arr2}\n')
    data.write(f'\n{new_arr[0]} + {new_arr2[0]}\n')
    data.write(f'{new_arr[1]} + {new_arr2[1]}\n')
    data.write(f'{new_arr[2]} + {new_arr2[2]}\n')
