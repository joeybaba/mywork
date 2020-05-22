#!/usr/local/bin/python3
# coding:UTF-8

"""函数式编程"""


# 偏函数前
def int2(x, base=2):
    print(type(base))
    relt = int(x, base)
    return relt


a = int2('11111')
b = int2('11111', 10)

# 创建偏函数
import functools

int10 = functools.partial(int, base=10)
int10('452')

print(callable(int10))


# 闭包
def outer(a):
    def inter():
        print('i in')
        return int10(a)


    return inter


c = outer('124')
c()


print('___________')
# map()函数
# 原函数
def normalize(name):
    lists = []
    if type(name) != list:
        raise ValueError("print put in a 'list'")
    for i, v in enumerate(name):
        lists.append(v[0].upper() + v[1:].lower())  # 列表为空时，需用append增加
    return lists
print(normalize(['SDdd', 'dsds']))
# 改写
def normalizes(name):
    return name[0].upper() + name[1:].lower()
lists = map(normalizes, ['adg', 'DDFff'])
print(list(lists))


# reduce()求积
from functools import reduce
def pord(s):
    idx = s.index('.')
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    start = map(lambda x: DIGITS[x], s[0:idx])
    end = map(lambda x: DIGITS[x], s[idx+1:])
    start_1 = reduce(lambda x, y: x*10+y, start)
    start_2 = reduce(lambda x, y: x*10+y, end)
    result = start_1 + start_2/100
    print(result)
    return result
pord('1234.51234234234')


# 递归函数 尾递归函数
def fact(n):
    if n ==1:
        return 1
    return n * fact(n-1)
# 尾递归函数
def facts(n):
    relt = 1
    def fact(n, relt):
        if n == 1:
            return relt
        return fact(n-1, relt * n)
    return fact(n, relt)
print(facts(4))

# 关键字参数 可变参数
# *nums表示把nums这个list的所有元素作为可变参数传进去 关键字参数
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数,**nums关键字参数在函数内部自动组装为一个dict
a = [1, 2, 'v']
b = dict(a = 1, b = 2)

print(*a)
print(*b)
def test(*args, **kwargs):
    print(args,kwargs)
test(*a,**b)
test(*b,**b)


