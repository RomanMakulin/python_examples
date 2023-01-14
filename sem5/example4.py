# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('file_encode.txt', 'w') as data:
    data.write('WWWWBWWBBBWB')

with open('file_encode.txt', 'r') as data:
    string = data.readline()
data.close

result = ''
i = 0
while i < len(string):
    count = 1
    while i + 1 < len(string) and string[i] == string[i + 1]:
        count += 1
        i += 1
    result += str(count) + string[i] + ' '
    i += 1

print(result)  
