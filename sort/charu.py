l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)

for i in range(lenght):
    for j in range(i):
        if l[i] < l[j]:
            l.insert(j, l.pop(i))
            break


print(l)
