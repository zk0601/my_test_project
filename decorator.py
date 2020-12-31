def decorator(func):
    def wrap(a, *args, **kwargs):
        print('555')
        if a == 1:
            return tt()
        else:
            return func(a, *args, **kwargs)
    return wrap


def ppp(func):
    def warp(a, *args, **kwargs):
        print('3333')
        return func(a, *args, **kwargs)
    return warp

# 第一个返回func则继续执行下一个decorator，否则则不执行下一个
@decorator
@ppp
def test(a):
    print(a)


def tt():
    print('2222')


if __name__ == '__main__':
    test(1)
