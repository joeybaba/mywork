# coding:utf-8


# 类的方法、属性用法、继承说明
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性外部无法直接访问
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
        self.f = ['v']

    def speak(self):
        print("%s say : i am %d." % (self.name, self.age))


p = People('Python', 10, 20)
p.speak()
# p.__weight 无法直接访问
print(p.name, '--', p.age)  # ,'--',p.__weight)


class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类方法
    def speak():
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class Speak():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    # 普通方法，对象调用
    def speak(self):
        tops = self.topic
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

    # 私有方法，self调用,类的内部调用
    def __song(self):
        print('唱一首歌自己听__song', self);

    # 静态方法，对象和类调用，不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的
    @staticmethod
    def song():
        print('唱一首歌给类听1:静态方法');

    # 普通方法，对象调用
    def song(self):
        print('唱一首歌给你们听2', self);

    # 类方法，对象和类调用，不能和其他方法重名，不然会相互覆盖，后面定义的会覆盖前面的
    @classmethod
    def song(self):
        print('唱一首歌给类听:类方法3', self)


class Sample(Speak, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speak.__init__(self, n, t)


test = Sample('Song', 24, 56, 7, 'Python')
test.speak()
test.song()
Sample.song()
test.song()
# test.__song() 无法访问私有方法
test = Speak('name', 'mini')
print(test.speak())


# 运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '111Vector(%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)  # 先调用add，后调用str
