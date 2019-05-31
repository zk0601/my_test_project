# 每次循环通过标记，只调换一个值的位置

l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)

for i in range(lenght):
    x = i
    for j in range(i+1, lenght):
        if l[j] < l[x]:
            x = j
    l[x], l[i] = l[i], l[x]
    print(l)


print(l)
