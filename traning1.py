# testing example

string = ['22', '23x', '3']
new_string = []

for i in string:
    if i.__contains__('x'):
        for j in i:
            if j == 'x':
                break
            new_string.append(j)
    else:
        new_string.append(i)        
print(new_string)

