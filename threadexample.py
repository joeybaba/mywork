# coding:UTF-8

"""线程的使用"""

import time
import threading
from threading import Semaphore, Lock, Event
import random
import logging
from queue import Queue


# 单线程和多线程比较
def compare():
    def profile(func):
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            func(*args, **kwargs)
            print(f'cost: {(time.perf_counter() - start)}')

        return wrapper

    # 斐波那契数列
    def fibfunc(x):
        def fib(x):
            if x == 2 or x == 1:
                return 1
            return fib(x - 1) + fib(x - 2)

        for i in range(1, x):
            # fib(i)
            print(fib(i), end=',')
        print('\n')

    @profile
    def nothread():
        fibfunc(10)
        fibfunc(10)

    @profile
    def hasthread():
        for i in range(2):
            t = threading.Thread(target=fibfunc, args=(10,))
            t.start()

        main_threading = threading.currentThread()
        for i in threading.enumerate():
            if i is main_threading:
                continue  # 直接跳转重新循环
            i.join()  # 等待两条子线程同步

    nothread()
    hasthread()


# 防止不同的线程同时对一个公用的资源（比如全部变量）进行修改，需要进行同时访问的数量（通常是 1）。
# 信号量同步基于内部计数器，每调用一次 acquire ()，计数器减 1；每调用一次 release ()，计数器加 1. 当计数器为 0 时，acquire () 调用被阻塞
def addsemaphore():
    sema = Semaphore(3)

    def foo(tid):
        sema.acquire()
        print('get:', tid)
        time.sleep(1)
        print('release:', tid)
        sema.release()

    def foo1(tid):
        with sema:
            print('get:', tid)
            time.sleep(1)
            print('release:', tid)

    thread = []

    for i in range(1, 6):
        t = threading.Thread(target=foo, args=(i,))
        thread.append(t)
        t.start()

    for i in thread:
        i.join()


# 加锁
def addlock():
    lock = Lock()
    value = 0

    def foo():
        nonlocal value
        # lock.acquire()
        new = value + 10
        time.sleep(0.0001)  # 让多个线程有机会切换
        value = new
        # lock.release()

    def foo1():
        nonlocal value
        with lock:
            value = value - 1

    thread = []

    for i in range(1, 10):
        t = threading.Thread(target=foo)
        thread.append(t)
        t.start()

    for i in thread:
        i.join()

    print(value)


# 一个线程等待特定条件，而另一个线程发出特定条件满足的信号
def addcondition():
    def consumer(cond):
        with cond:
            print('i am waiting')
            cond.wait()
            print('i in consumer!')

    def producer(cond):
        with cond:
            print('i in producer1')
            cond.notifyAll()
            print('i in notify')

    condition = threading.Condition()
    p = threading.Thread(target=producer, args=(condition,))
    c = threading.Thread(target=consumer, args=(condition,))

    c.start()
    time.sleep(1)
    p.start()
    c.join()
    p.join()


# 一个线程发送/传递事件，另外的线程等待事件的触发
def addevent():
    def consumer(event, args):
        while 1:
            try:
                eventresult = event.wait(timeout)
                print(eventresult)
                if eventresult is True:
                    result = args.pop()  # 有时候会全部pop掉元素，之后报错
                    print(result)
                    event.clear()
            except IndexError as e:
                logging.exception(e)
                # print(e)
                # print('i in IndexError')
                pass

    def producer(event, args):
        while 1:
            num = random.randint(0, 100)
            args.append(num)
            event.set()
            time.sleep(1)

    timeout = 1
    args = []
    event = threading.Event()

    c = threading.Thread(target=consumer, args=(event, args))
    p = threading.Thread(target=producer, args=(event, args))

    c.start()
    p.start()
    c.join()
    p.join()


# 线程中进行通讯
# 全局变量修改要加锁，每个线程的局部变量都只能读写自己线程的独立副本，互不干扰,不用加锁
# 最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等,这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源
def threadlocal():
    local_value = threading.local()

    def consumer():
        print(local_value.name)

    def producer(n):
        local_value.name = n
        print(threading.current_thread())
        consumer()

    threadlist = []
    for i in range(3):
        t = threading.Thread(target=producer, args=[i, ])
        t.start()
        threadlist.append(t)

    for i in threadlist:
        i.join()


if __name__ == '__main__':
    # addsemaphore()
    # addlock()
    # addcondition()
    # addevent()
    threadlocal()
