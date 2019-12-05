from functools import wraps


# 普通的简单装饰器
def decorator(func):
    def inter(*args, **kwargs):
        func(*args, **kwargs)
        print('1')
    return inter


# 使得fun的__name__和__doc__正常显示
def decorator1(func):
    @wraps(func)
    def inter(*args, **kwargs):
        func(*args, **kwargs)
        print('1')
    return inter


@decorator1
def work(a, b='b', **kwargs):
    print(a, b)
    print(**kwargs)


if __name__ == '__main__':
    work('a')
    print(work.__name__)
    raise ImportError
