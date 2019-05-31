# 分治思想，一直拆分直到2个数，然后把每个子有序数列再合起来

l = [4,5,6,7,3,2,6,9,8,1]
lenght = len(l)


def func(l):
    def chai(l):
        if len(l) == 1:
            return l
        mid = len(l)//2
        left = chai(l[:mid])
        right = chai(l[mid:])
        return he(left, right)

    def he(l, r):
        result = []
        while l and r:
            if l[0] < r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        if l:
            result += l
        else:
            result += r
        return result

    return chai(l)

print(func(l))
