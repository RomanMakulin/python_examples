# 4.Саша и Галя коллекционируют монетки. 
# Каждый из них решил записать номиналы монеток из своей коллекции. 
# Получилось два списка. Эти списки поступают на вход программы 
# в виде двух строк из целых чисел, записанных через пробел. 
# Необходимо выделить значения, присутствующие в обоих списках 
# и оставить среди них только четные. Результат вывести на экран 
# в виде строки полученных чисел в порядке их возрастания через пробел.

# При реализации программы используйте функцию filter 
# # и кое-что еще (для упрощения программы), подумайте что.

list1 = '2 2 3 4 12 2 3 4 12 2 3 4 12 2 3 4 12 2 3'
array1 = []
list2 = '8 2 5 7 2 1 18 2 5 7 2 1 18 2'
array2 = []
new_arr = []

import time
start = time.time()

# 0.1900196075439453 ms
def moneta(list2, array2):
    for i in list2:
        if i != ' ':
            i = int(i)
            array2.append(i)
    array2 = list(filter(lambda i: not i%2, array2))
    return array2

result_list = moneta(list2, array2) + moneta(list1, array1)
print(', '.join([str(i) for i in result_list]))

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")
