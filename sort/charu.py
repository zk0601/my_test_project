# 循环前面已经排序好的队列，后面依次进行插入

l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)

for i in range(lenght):
    for j in range(i):
        if l[i] < l[j]:
            l.insert(j, l.pop(i))
            break


print(l)
