#!/usr/bin/env python
# coding:UTF-8

"""quicksort.py"""


def quicksort1(alist, left, right):  # 第一种快速排序，pivot选最左边，left=0，right=len(alist)
    if left > right:  # 限制右边溢出
        return 1
    l, r = left, right
    pivot = alist[left]

    while l != r and l < r:

        while pivot <= alist[r] and l < r:
            r -= 1

        if pivot > alist[r] and l < r:
            alist[l] = alist[r]
            l += 1

        while pivot >= alist[l] and l < r:
            l += 1

        if pivot <= alist[l] and l < r:
            alist[r] = alist[l]
            r -= 1

    print(l, r)

    if l == r:
        alist[l] = pivot
        quicksort1(alist, left, r - 1)
        quicksort1(alist, r + 1, right)


def quicksort2(alist, left, right):  # 第二种快速排序，pivot选最左边，不和left同一位置，left=1，right=len(alist)
    if left > right:
        return 1

    l = left
    r = right
    pivot = alist[l]

    while l < r:
        while l < r and pivot >= alist[l]:
            l += 1

        while l < r and pivot <= alist[r]:
            r -= 1

        if l < r:
            alist[l], alist[r] = alist[r], alist[l]

    if l == r:
        alist[left] = alist[l]
        alist[l] = pivot

    quicksort2(alist, left, r - 1)
    quicksort2(alist, r + 1, right)


if __name__ == '__main__':
    alist = [6, 1, 2, 3, 4]
    quicksort1(alist, 0, len(alist) - 1)
    quicksort2(alist, 0, len(alist) - 1)
    print(alist)
