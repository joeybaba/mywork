# coding:UTF-8
"""线程的使用"""
import os
import time
import multiprocessing

# 单进程和多进程比较
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
            print(fib(i), end=',')
        print('\n')

    @profile
    def nomultiprocessing():
        for i in range(10):
            fibfunc(10)
            fibfunc(10)
            fibfunc(10)
            fibfunc(10)
            fibfunc(10)
            fibfunc(10)

    @profile
    def hasmultiprocessing():
        for i in range(10):
            p = multiprocessing.Process(target=fibfunc, args=(10, ))
            # t = threading.Thread(target=fibfunc, args=(10,))
            p.start()

        # main_threading = multiprocessing.current_process()
        child = multiprocessing.active_children()

        for i in child:
            i.join()  # 阻塞，等待两条子进程同步

    hasmultiprocessing()
    nomultiprocessing()


# 进程池pool
# 斐波那契数列
def fibfuncs(x):
    def fib(x):
        if x == 2 or x == 1:
            return 1
        return fib(x - 1) + fib(x - 2)

    for i in range(1, x):
        print(fib(i), end=',')
    print('\n')

    pool = multiprocessing.Pool(4)
    pool.map(fib, [35] * 2)
    # pool.map(lambda x: x + 1, [35] * 2)  # 错误
    pool.close()
    pool.join()


# 进程中通讯 Queue
def addqueue():
    def writer(q):
        for i in [1, 2, 3]:
            q.put(i)

    def read(q):
        while 1:
            print('i in')
            value = q.get(True)
            print(value)

    # 直接运行
    # q = multiprocessing.Queue()
    # wp = multiprocessing.Process(target=writer, args=(q,))
    # rp = multiprocessing.Process(target=read, args=(q,))
    # wp.start()
    # rp.start()
    # wp.join()
    # rp.join()

    # pool的方式，调用函数要topl-evel
    m = multiprocessing.Manager()
    q = m.Queue()
    pool = multiprocessing.Pool(4)
    pool.apply_async(writer, args=(q, ))
    pool.apply_async(read, args=(q, ))
    pool.close()
    pool.join()

    # RuntimeError: Queue objects should only be shared between processes through inheritance
    # 大意是队列对象不能在父进程与子进程间通信，这个如果想要使用进程池中使用队列则要使用multiprocess的Manager类,不用池则不需要Manager
    # 函数里面是子进程。。。main()里是主进程


if __name__ == '__main__':
    compare()

    # # addpool()  # AttributeError: Can't pickle local object 'addpool.<locals>.fib'
    # # pickle是用来序列化对象很方便的工具，但是pickle对传入对象的要求是不能是内部类，也不能是lambda函数
    # # 有些类型的对象是不能被序列化的。这些通常是那些依赖外部系统状态的对象， 比如打开的文件，网络连接，线程，进程，栈帧等等。
    # # 用户自定义类可以通过提供__getstate__()和__setstate__()方法来绕过这些限制。
    # # 父进程的内容经过序列化才能送至子进程
    # def runpool():
    #     pool = multiprocessing.Pool(4)
    #     pool.map(fibfuncs, [35] * 2)
    #     # pool.map(lambda x: x + 1, [35] * 2)  # 错误
    #     pool.close()
    #     pool.join()
    # runpool()
    # addqueue()
