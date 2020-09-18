class Test:
    name = 'Testhahahaha'

    # self:描述符对象n, instance:实例t1, owner:t1所属的类Test1
    def __get__(self, instance, owner):
        print('====>get')
        print(self, instance, owner, sep='\n')
        return self

    def __set__(self, instance, value):  # value:值3
        print('====>set')
        print(self.name, instance, value, sep='\n')
        instance.__dict__['n'] = value

    def __delete__(self, instance):
        print('====>delete')
        print(self, instance)


class Test1:
    n = Test()
    def __init__(self, name):
        self.name = name

nn = Test1('a')
nn.n = 1
nn.n

# Test1.n  # 类调用属性会触发__get__
# print('=====>hahaha')
# t1 = Test1('sabi')  # 不涉及属性n时不会触发描述符
# t1.n = 3  # 触发__set__, 增加属性n,但类属性不变
# print(t1.__dict__)
# print(t1.n)  # 触发__get__
# del t1.n  # 触发__delete__
# print('=====分隔')
# del Test1.n  # 类删除属性也不会触发__delete__



