# type()创建类
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