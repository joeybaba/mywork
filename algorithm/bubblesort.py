#!/usr/bin/env python
# coding: UTF-8

"""bubblesort.py"""


def bubble_sort(alist):
    alen = len(alist)
    count = 0  # 测试是否有序序列
    for i in range(alen - 1):
        for j in range(alen - 1 - i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
                count = 1
        if count == 0:
            print('error')
            break


if __name__ == '__main__':
    alist = [1, 2, 9, 4, 8]
    bubble_sort(alist)
    print(alist)
