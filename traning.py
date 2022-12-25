# Палиндром
string = '12211'

count = len(string)
a = False

for i in range(len(string)//2):
    if string[i] == string[count-1]:
        a = True
    else:
        a = False
        break
    count -= 1

print(a)
