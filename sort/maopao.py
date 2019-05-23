l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)

# for i in range(lenght):
#     for j in range(i+1, lenght):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]
#     print(l)

for i in range(lenght):
    for j in range(lenght-i-1):
        if l[j] > l[j+1]:
            l[j+1], l[j] = l[j], l[j+1]
    print(l)


print(l)
