# 二分思想，递归将每段数列分为两段

l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)

def func(l):
    if l == []:
        return []
    flag = l[0]
    left, right = [], []
    for i in l[1:]:
        if i < flag:
            left.append(i)
        else:
            right.append(i)
    left = func(left)
    right = func(right)
    return left + [flag] + right

print(func(l))
