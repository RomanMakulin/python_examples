# Больше предыдущего
# На вход программе подается строка из текста из натуральных чисел.
# Из нее формируется список чисел. Написать программу подсчета количества чисел,
# которые больше предыдущего им в этом списке числа, то есть, стоят вслед за меньшим числом.

# Формат ввода данных: подается строка текста разделенных пробелами натур чисел
# Формат выходных данных: программа должна вывести одно число 
# - кол-во элементов списка, больших предыдущего

# 1 2 3 4 5
# 4

# 1 1 3 2 2 1 1 1 1
# 1

# 5 4 3 2 1
# 0

string = '1 1 3 2 2 1 1 1 1'
numbers = []
count = 0

for i in string:
    if i != ' ':
        numbers.append(int(i))

for i in range(len(numbers)-1):
    if numbers[i+1] > numbers[i]:
        count += 1
print(count)