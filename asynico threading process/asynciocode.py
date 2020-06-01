# coding:UTF-8

"""asyncio异步的应用"""
# https://www.dongwm.com/post/understand-asyncio-3/

import asyncio
import time
from functools import partial


def asyncio_func1():
    # 定义一个协程
    async def a():
        print('i in a()')
        i = 0
        i += 1
        await asyncio.sleep(1)

    # 定义一个协程
    async def b():
        print('i in b()')

    async def main():
        await asyncio.gather(a(), b())

# # 调用包装后的main()
# asyncio.run(main())

    # 旧方法
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # loop.run_until_complete(asyncio.gather(a(), b()))
    loop.close()

    # # 生成task后调用
    # tasks = asyncio.create_task([a(), b()])
    # asyncio.run(tasks)


# Eventloop 除了支持协程，还支持注册 Future 和 Task 2种类型的对象
# Future 是协程的封装，Future 对象提供了很多任务方法 (如完成后的回调、取消、设置任务结果等等)，
# 但是开发者并不需要直接操作 Future 这种底层对象，而是用 Future 的子类 Task 协同的调度协程以实现并发。
async def task_type():
    # 定义一个协程
    async def a():
        print('i in a()')
        i = 0
        i += 1
        await asyncio.sleep(1)

    # 定义一个协程
    async def b():
        print('i in b()')

    # 三种方法
    task = asyncio.ensure_future(a())

    loop = asyncio.get_event_loop()
    task = loop.create_task(a())

    # 这种方法要在协程里创建
    # 该任务会在 get_running_loop() 返回的loop中执行，如果当前线程没有在运行的loop则会引发 RuntimeError
    task = asyncio.create_task(a()) # 后面加上await task

    print(task.done())
    await task
    print(task.done())


# 用asyncio正确并发
def concurrency_control():
    # 定义一个协程
    async def a():
        print('i in a()')
        await asyncio.sleep(2)

    # 定义一个协程
    async def b():
        print('i in b()')
        await asyncio.sleep(1)

    # 错误的并发，只会串行运行
    async def s1():
        await a()
        await b()

    # 正确
    async def s2():
        task1 = asyncio.create_task(a())
        task2 = asyncio.create_task(b())
        await task1
        await task2
        # 错误
        # await asyncio.create_task(a())
        # await asyncio.create_task(b())

    async def s3():
        await asyncio.gather(a(), b())

    async def s4():
        tasks = [asyncio.create_task(a()) for i in range(3)]
        await asyncio.gather(*tasks)
        for task in tasks:
            print(task.result())

    # 比较运行时间的函数
    def show_perf(func):
        print('*' * 20)
        start_time = time.perf_counter()
        asyncio.run(func())
        print(f'{func.__name__} Cost: {time.perf_counter() - start_time}')

    show_perf(s1)
    show_perf(s2)
    show_perf(s3)
    show_perf(s4)


# asyncio.gather()方法的名字说明了它的用途，gather 的意思是「搜集」，也就是能够收集协程的结果，
# 而且要注意，它会按输入协程的顺序保存的对应协程的执行结果
# 参数可以为task
def asyncio_gather():
    # 定义一个协程
    async def a():
        print('i in a()')
        i = 0
        i += 1
        await asyncio.sleep(1)
        return 1

    # 定义一个协程
    async def b():
        print('i in b()')
        return 2

    async def run1():
        A, B = await asyncio.gather(a(), b())  # 不接收列表
        print(A, B)
        # 另一种打印方式
        print(f'{A} {B}')

    asyncio.run(run1())


# 成功回调
# 可以给 Task (Future) 添加回调函数，等 Task 完成后就会自动调用这个 (些) 回调
def callback_1():
    async def a():
        await asyncio.sleep(1)
        return 1

    # 普通函数
    def callback(future):
        print(f'{future.result()}')

    def callback2(future, n):
        print(f'{future.result()},N:{n}')

    async def main():
        task = asyncio.create_task(a())
        task.add_done_callback(callback)
        task.add_done_callback(partial(callback2, n='input'))
        await task

    asyncio.run(main())


# 用run_into_executor可以把同步函数逻辑转化成一个协程
def sync():
    def a():
        time.sleep(1)
        print('i in sync()')
        return 'A'

    async def b():
        await asyncio.sleep(1)
        print('i in b()')
        return 1

    async def main():
        loop = asyncio.get_event_loop()
        await asyncio.gather(loop.run_in_executor(None, a), b())
        # 第一个参数是要传递concurrent.futures.Executor实例的，传递None会选择默认的executor

    asyncio.run(main())


if __name__ == '__main__':
    # sync()
    # # callback_1()
    # # concurrency_control()
    # # asyncio_gather()
    # # asyncio.run(task_type())
    asyncio_func1()
