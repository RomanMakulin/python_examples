array = [10, 3, 1, 5, 2, 6, 5, 2, 1]
m = 3

max = 0


t = max
for j in range(len(array)-m):
    t = t - array[j -1] + array[j + (m - 1)]
    if t > max:
        max = t
    
print(max)