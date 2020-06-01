#!/usr/bin/env python
# coding: UTF-8

"""insertionsort.py"""


def insertionsort(alist):
    alen = len(alist)

    for i in range(1, alen, 1):
        key = alist[i]
        j = i - 1

        while alist[j] > key and j >= 0:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = key


if __name__ == '__main__':
    alist = [1, 5, 2, 6, 3, 9]
    insertionsort(alist)
    print(alist)
