"""
回溯模板
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""

# 全排列
list = [1, 2, 3]
ret = []
ret.extend(list)
def func(pp, ret):
    if len(pp) == len(list):
        print(pp)
    for i, va in enumerate(ret):
        pp.append(va)
        temp = ret[:]
        temp.pop(i)
        func(pp[:], temp)
        pp.pop(-1)

func([], ret)

