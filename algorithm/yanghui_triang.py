#!/usr/bin/env python
# coding: UTF-8


"""杨辉三角"""


def yanghui_triang(max):
    i = 1
    l = [1]
    while i <= max:
        l = [l[x] + l[x + 1] for x in range(len(l) - 1)]
        l.insert(0, 1)  # 头部插入元素
        l.append(1)  # 尾部增加元素

        i += 1
    return l


print(yanghui_triang(5))


# 生成器调用generator
def yanghui_triang(max):
    i = 1
    l = [1]
    while i <= max:
        yield l
        l = [l[x] + l[x + 1] for x in range(len(l) - 1)]
        l.insert(0, 1)
        l.append(1)

        i += 1


if __name__ == '__main__':
    for i in yanghui_triang(6):
        print(i)
