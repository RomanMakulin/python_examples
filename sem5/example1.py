# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

string = 'Childrensabc are playing game. They are need to compare box an abc'
new_string = [i for i in string.split() if 'abc' not in i]
print(' '.join(new_string))