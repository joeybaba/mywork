#!/usr/bin/env python
# coding: UTF-8

# https://www.bilibili.com/video/av94166791?from=search&seid=12118334399760597355


def h_sorting(alist, alen, ah):  # 做一次排序
    i = h = ah
    while i < alen:
        key = alist[i]
        j = i - h

        while j >= 0 and alist[j] > key:
            alist[j + h] = alist[j]

            j -= h

        alist[j + h] = key

        i += 1


def shellsort(alist, alen):  # 做h次增量递减序列排序

    h = alen / 2

    while h >= 1:
        h_sorting(alist, alen, h)
        h = h / 2

    #
    # h=[8, 4, 2, 1]
    #
    # for i in h:
    #     h_sorting(alist, alen, i)


if __name__ == '__main__':
    alist = [1, 3, 2, 5, 4, 6, 8, 9, 2, 9]
    shellsort(alist, len(alist))
    print(alist)
