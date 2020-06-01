#!/usr/bin/env python
# coding: UTF-8

"""网上摘取"""

import math


def shell_sort(a):
    n = len(a)
    gap = math.ceil(n / 2)  # gap是长的一半
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if a[j] < a[j - gap]:
                    a[j], a[j - gap] = a[j - gap], a[j]
                else:
                    break
        gap = int(gap / 2)  # gap每次减半


if __name__ == "__main__":
    a = [10, 4, 3, 1, 6, 20, 30, 1, 40, 30, 20]
    print(a)
    shell_sort(a)
    print(a)
