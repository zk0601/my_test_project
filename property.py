class A(object):
    def __init__(self):
        self._a = 1
        self.b = 2

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        print('set')
        self._a = value


if __name__ == '__main__':
    obj = A()
    print(obj.a)
    obj.a = 3
    print(obj.a)
