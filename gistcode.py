# coding:UTF-8

"""片段代码，同步到gist"""

# 已同步gist
# 查看模块（变量、函数、类）方法 忽略显示 dir() 函数输出的特殊成员的方法
import string
print([e for e in dir(string) if not e.startswith('_')])

# 查看模块成员：__all__变量
# __all__ 变量在查看指定模块成员时，它不会显示模块中的特殊成员，同时还会根据成员的名称进行排序显示
# 并非所有的模块都支持使用 __all__ 变量，因此对于获取有些模块的成员，就只能使用 dir() 函数
import string
print(string.__all__)

# vars() __dict__ 返回所有变量字典
# vars([object]) 返回object对象的__dict__属性，其中object对象可以是模块，类，实例，或任何其他有__dict__属性的对象。
mm.__dict__
{'__name__': 'mm', '__doc__': None, '__package__': ''}


# input()输入多行数据小窍门
lines = []
while True:
    try:
        lines.append(input())
    except:
        break

print(lines)
# 第二种
from sys import stdin
while True:
    value = stdin.readline()

# exec语句执行代码。exec执行一系列Python语句，而eval计算用字符串表示的Python表达式的值
exec("""for i in [1,2]:
    print(i)
    print(i)""")
dictsc = {}
exec("a = 1",dictsc)
print(type(dictsc))


# logging记录错误，logging.exception(e)显示错误后继续执行
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
print('i in')
# 继续运行代码不中断
try:
    self.importfunc = __import__(self.package)
    self.__createtext()
except Exception as e:
    logging.exception(e)  # 显示错误后继续执行
    self.importfunc = None


# match() 起始位置匹配 re.match(pattern, string, flags=0)
import re
print(re.match('com', 'wwww.runoob.wwwwcom'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print
    "No match!!"

# re.search() 扫描整个字符串并返回第一个成功的匹配 re.search(pattern, string, flags=0)
line = "Cats are smarter than dogs";
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)
if searchObj:
    print"searchObj.group() : ", searchObj.group()
    print"searchObj.group(1) : ", searchObj.group(1)
    print"searchObj.group(2) : ", searchObj.group(2)
else:
    print"Nothing found!!"


# re.sub()用于替换字符串中的匹配项 re.sub(pattern, repl, string, count=0, flags=0)
import re
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

# __str__ 和 __repr__说明
class A():
    def __repr__(self):
        return 'i in repr'

    def __str__(self):
        return 'i in str'

a = tempcode2.A()
a
i in repr
print(a)
i in str

# python 调用shell命令 系统命令 cmd
import os, sys
cmd = sys.stdin.readline()
os.system(cmd)


# Shell
# Shell 是指一种应用程序，这个应用程序提供了一个界面，用户通过这个界面访问操作系统内核的服务。
# 一说到命令行，我们真正指的是 shell。shell 就是一个程序，它接受从键盘输入的命令， 然后把命令传递给操作系统去执行。几乎所有的 Linux 发行版都提供一个名为 bash 的 来自 GNU 项目的 shell 程序。
# “bash” 是 “Bourne Again SHell” 的首字母缩写， 所指的是这样一个事实，bash 是最初 Unix 上由 Steve Bourne 写成 shell 程序 sh 的增强版。


# 切分空格的问题
>>> 'a b   c'.split(' ')
['a', 'b', '', '', 'c']  # ''里的是空字符，不是' '


# 正则表达式预编译 避免重复调用
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')

# pip下的文件夹权限所有错误
# WARNING: The directory '/Users/joey/Library/Caches/pip' or its parent directory is not owned
# or is not writable by the current user. The cache has been disabled.
sudo chown -R root /Users/joey/Library/Caches/pip

# 格式化输出 f
%m.nf，m为指定的输出字段的宽度。如果数据的位数小于m，则左端补以空格，若大于m，则按实际位数输出。
n为保留n位小数

# re模块先编译后比较
>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')


# pip-review包使用问题 -换为_
python3 -m pip_review --local --interactive
#pip包本地安装方法 python3 setup.py install

# 枚举类及唯一性
from enum import Enum
from enum import unique

@unique
class Color(Enum):
    red = 1
    green = 2
    blue = 3


# 下划线定义
# _xxx 这表示这是⼀个保护成员（属性或者⽅法），它不能⽤from module import * 导⼊，其他⽅⾯和公有⼀样访问；
# __xxx 这表示这是⼀个私有成员，它⽆法直接像公有成员⼀样随便访问（⽐如直接print阿修改阿），当然，要想访问也可以，通过对象名._类名__xxx这样的⽅式可以访问；
# __xxx__ 这表示这是⼀个特殊成员，所谓特殊，就是例如__init__() __del__() __call__()这些niubi哄哄
# 的特殊⽅法

# #!/usr/bin/env python作用
# Just to add: this applies when you run it in Unix by making it executable (chmod +x myscript.py) and then running it directly: ./myscript.py, rather than just python myscript.py.

# __setattr__和__getattr__
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

# TODO

__未同步