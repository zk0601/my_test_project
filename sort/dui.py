# 使用大根堆，即完全二叉树，构造树，然后取出将根节点和最后叶节点交换，取出最后叶节点，再构造树，循环直到树为空

l = [4,5,6,7,3,2,6,9,8,1]


def heapify(l, i):
    lenght = len(l)
    if i >= lenght:
        return
    m, c1, c2 = i, 2*i+1, 2*i+2
    if c1 < lenght and l[c1] > l[m]:
        l[m], l[c1] = l[c1], l[m]
    if c2 < lenght and l[c2] > l[m]:
        l[m], l[c2] = l[c2], l[m]
    heapify(l, c1)
    heapify(l, c2)


def build_tree(l):
    last_root = (len(l)-2) // 2
    for i in range(last_root, -1, -1):
        heapify(l, i)


def func(l):
    lenght = len(l)
    result = []
    while lenght > 0:
        build_tree(l)
        l[lenght-1], l[0] = l[0], l[lenght-1]
        result.insert(0, l.pop())
        lenght = len(l)
    return result


print(func(l))
