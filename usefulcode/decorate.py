# coding:UTF-8

"""函数装饰器"""

import functools


def decoratetest(cls):
    """decorate doc"""

    @functools.wraps(cls)
    def warpper(*args, **kwargs):
        print('v')
        return cls(*args, **kwargs)

    return warpper


def decorater_text(text):
    def receptiontext(cls):
        @functools.wraps(cls)
        def warpper(*args, **kwargs):
            print('在装饰器里面调用函数也可以')
            print(text)
            return cls(*args, **kwargs)

        return warpper

    return receptiontext


class Decorater(object):

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args):
        print("包装内容")
        return self.cls(*args)


@decoratetest
class UserDataBase(object):
    """user doc"""

    def __init__(self, filepath):
        self.filepath = filepath

    def isexist(self):
        return self.username


@decorater_text('imformation')
class Test(object):
    def a(self):
        print('Test', 'r')


@Decorater
def test():
    print("主函数")


a = UserDataBase('')
print(dir(a))
print(a.__dict__)

b = Test()
print(b.__doc__)

c = test()
print(c.__doc__)


# _____________________________________


# @property 像调用属性一样调用类的方法
class Student(object):
    __slots__ = ('_score', 'nn')

    @property
    def score(self):
        print('in score')
        return self._score

    @score.setter
    def score(self, value):
        print('in setter score')
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.score = 98
print(s.score)


# @property 像调用属性一样调用类的方法
class C(object):
    __slots__ = ('_x', 'y')

    @property
    def x(self):
        print("I am the 'x' property.")
        return self._x

    @x.getter
    def x(self):
        print("getter")
        return self._x

    @x.setter
    def x(self, value):
        print("setter")
        self._x = value

    @x.deleter
    def x(self):
        print("deleter")
        del self._x


c = C()
c.x = 100
