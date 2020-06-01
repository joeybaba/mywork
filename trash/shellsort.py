#!/usr/bin/env python
# coding:UTF-8

'shellsort.py'
# TODO 错误算法

def shellsort(alist):
    alen= len(alist)

    blist=[]
    k= alen
    while k> 1:
        blist.append(k/2)
        k/= 2

    for k in blist:
        if k== 1:
            break
        for i in range(k):
            n= 0
            while i+n*k<= alen-1:
                if alist[i]> alist[i+n*k]:
                    alist[i], alist[i+n*k]= alist[i+n*k], alist[i]
                n+= 1
    print 'k>1时处理后的序列：', alist

    for i in range(1,alen):
        key =alist[i]
        j= i-1
        while j>=0 and alist[j]> key:
            alist[j+1]= alist[j]
            j-= 1
        alist[j+1]= key
    print 'k=1时调用直接插入算法处理后的结果：', alist


if __name__ == '__main__':
    alist=[1, 2, 5, 3, 4, 4, 2, 4, 1, 2, 3, 4]
    shellsort(alist)

# algorithm 错误，看shellsort1.py
