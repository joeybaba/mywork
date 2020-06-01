#!/usr/bin/env python
# coding:UTF-8

"""selectionsort.py"""


def selectionsort(alist):
    alen = len(alist)
    for i in range(alen):  # 最小值遍历
        key = alist[i]  # 记录最小值位置以及值
        keynum = i
        for j in range(i, alen, 1):  # 找到最小值
            if key > alist[j]:
                key = alist[j]
                keynum = j
        alist[keynum] = alist[i]  # 替换最小值
        alist[i] = key


if __name__ == '__main__':
    alist = [11, 1, 41, 161, 21, 81, 31, 12]
    selectionsort(alist)
    print(alist)


def selection_sort(alist):
    for i in range(0, len(alist)):
        min = alist[i]
        index = i
        for j in range(i, len(alist)):
            if alist[j] < min:
                min = alist[j]
                index = j
        tmp = alist[i]
        alist[i] = min
        alist[index] = tmp
        print(alist)


alist = [54, 26, 2, 2, 77, 31, 44, 55, 20]
print('old:', alist)
selection_sort(alist)
print('new:', alist)
