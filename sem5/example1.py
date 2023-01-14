# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
with open('sem5/file.txt', 'r') as data:
    string = data.read()
data.close

new_string = [i for i in string.split() if 'abc' not in i]
print(' '.join(new_string))