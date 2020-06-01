# coding:UTF-8


# __setattr__和__getattr__说明
class TestGetattr(object):
    # 如果设置__setattr__，__getattr__要一起出现
    def __getattr__(self, item):  # 默认返回None
        print('getattr')
        if item == 'xx':
            return 1
        else:
            raise ValueError('no allow to getattr:', item)
        # return lambda: 25  # 返回函数也可以

    def __setattr__(self, key, value):
        return value
        # self.key = value  # 不能这样设置，会反复调用__setattr__

    def __getitem__(self, item):
        pass


print('_________')
t = TestGetattr()
t.xx = 2
print(t.xx)


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


print('_____________')
s = Student()
s.score = 98
print(s.score)


# type()创建函数
def func(self,name):
    print('s')
    print(name)

def init(self,b):
    self.b = b
    print('__init__')


dicts = dict(hello=func, __init__=init)
Hello = type('Hello', (object,), dicts)  # 传入字典，不是关键字参数
a = Hello('b')
a.hello('name')