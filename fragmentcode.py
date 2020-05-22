# coding:UTF-8

"""片段代码，含同步gist的"""

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


