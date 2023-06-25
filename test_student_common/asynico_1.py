
from greenlet import greenlet

#
# def fun1():
#
#     print('1')      # 第一步输出1
#     gr2.switch()     # 切换后代码块走到这里，调用fun2函数
#
#     print('2')       # 上面走过，从这里开始运行，打印2
#
#     gr2.switch()        # 切换后代码块走到这里，再调用fun2函数
#
#
# def fun2():
#
#     print('3')    # 然后执行这个，打印3
#     gr1.switch()   # 切换后代码块走到这里，调用fun1函数
#     print('4')      # 再从这里打印，然后结束
#
#
# gr1 = greenlet(fun1)
# gr2 = greenlet(fun2)
#
#
# gr1.switch()    # 全部走完
# gr2.switch()    # 不走2，打印4吗，就结束了


# def fun3():
#
#     yield 1       # 运行 返回1
#
#     yield from fun4()       # 调用函数4 ，依次返回  3， 4，执行完成
#
#     yield 2     # 返回2
#
#
# def fun4():
#
#     yield 3
#     yield 4
#
#
# f1 = fun3()    # 获取的是个对象
# for item in f1:
#     """循环取"""
#     print(item)


import asyncio


# @asyncio.coroutine    # coroutine 协程意思
# def fun5():
#
#     print('1')
#     yield from asyncio.sleep(2)    # 遇到IO耗时操作。自动化切换tasks中其他任务
#     print('2')
#
#
# @asyncio.coroutine
# def fun6():
#
#     print(3)
#
#     yield from asyncio.sleep(2)    # 遇到IO耗时操作。自动化切换tasks中其他任务
#
#     print(4)
#
#
# tasks = [asyncio.ensure_future(fun5()),
#          asyncio.ensure_future(fun6())]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))


# async def fun7():
#
#     print(1)
#
#     await asyncio.sleep(2)
#
#     print(2)
#
#
# async def fun8():
#
#     print(3)
#
#     await asyncio.sleep(2)
#
#     print(4)
#
# tasks = [asyncio.ensure_future(fun7()),
#          asyncio.ensure_future(fun8())]
# # 去生成或获取一个事件循环，
# loop = asyncio.get_event_loop()
# # 将任务放到‘任务列表； tasks是任务
# loop.run_until_complete(asyncio.wait(tasks))


import requests


# def down_load(url):
#     """同步方法"""
#     print("下载开始")
#     rs = requests.get(url)
#     print("下载完成")
#     # file_name = url.split('/')[-1] + '.png'
#
#     with open('33.png', mode='wb')as f:
#
#         f.write(rs.content)

# import aiohttp
# import asyncio
# import aiofiles
#
#
# async def down_load(session, url):
#     """异步方法"""
#     print("发送请求", url)
#
#     async with session.get(url, verify_ssl=False) as response:
#         content = await response.content.read()
#
#     for a in range(1, 4):
#         """循环取名字，"""
#         file_name = str(a) + '.png'
#
#         async with aiofiles.open(file_name, mode='wb')as f:
#
#             await f.write(content)
#     print('下载完成', url)
#
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#
#         url_list = [
#             "https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF",
#             "https://t7.baidu.com/it/u=3569419905,626536365&fm=193&f=GIF",
#             "https://t7.baidu.com/it/u=3124693600,356058981&fm=193&f=GIF"
#         ]
#
#         tasks = [asyncio.create_task(down_load(session, url)) for url in url_list]
#
#         await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#
#     asyncio.run(main())


# async def fun77():
#
#     print(3)
#
# rs = fun77()


# loop = asyncio.get_event_loop()     # 创建事件循环
# loop.run_until_complete(rs)         # 将任务放到任务列表执行
# asyncio.run(rs)   # 运行协程对象


# async def funs():
#
#     print('333')    # 到这里 打印
#
#     await asyncio.sleep(2)  # 协程等待
#
#     print('end')    # 到这里打印
#
#     return "返回值"        # 到这里返回值，这个函数结束
#
#
# async def su():
#
#     print("执行协程函数内部代码")     # 先执行su，到第一步打印
#
#     res = await funs()      # 到这儿，调用 跳到上， 调用得到返回值
#
#     print("IO请求结果为：", res)   # 最后一步。打印结果
#
#     res2 = await funs()      # 到这儿，调用 跳到上， 调用得到返回值
#
#     print("IO请求结果为：", res2)   # 最后一步。打印结果
#
# sd = su()
#
# asyncio.run(sd)


# async def funx():
#
#     print(1)
#
#     await asyncio.sleep(2)
#
#     print(2)
#
#     return "返回值"
#
#
# async def main():
#
#     print("main开始")
#     """依次创建task对象,里面传入协程对象添加到事件循环"""
#     task1 = asyncio.create_task(funx())    # 切换
#
#     task2 = asyncio.create_task(funx())     # 切换
#
#     print("main--end")      # 没有io 到这边,不等待, 先打印了
#
#     ret1 = await task1      # 等待 切换到对应协程函数内容
#
#     ret2 = await task2
#
#     print(ret1, ret2)
#
#
# asyncio.run(main())


# async def funx():
#
#     print(1)
#
#     await asyncio.sleep(2)
#
#     print(2)
#
#     return "返回值"
#
#
# async def main():
#
#     print("main开始")
#     """依次创建task对象,里面传入协程对象添加到事件循环"""
#     # task1 = asyncio.create_task(funx())    # 切换
#     #
#     # task2 = asyncio.create_task(funx())     # 切换
#
#     task_list = [
#         asyncio.create_task(funx(), name='n1'),
#         asyncio.create_task(funx(), name='n2')
#     ]
#
#     print("main--end")      # 没有io 到这边,不等待, 先打印了
#
#     done, pending = await asyncio.wait(task_list, timeout=None)
#
#     print(done)
#
#
# asyncio.run(main())


# async def funx():
#     print(1)
#
#     await asyncio.sleep(2)
#
#     print(2)
#
#     return "返回值"
#
#
# task_list = [
#        funx(),
#        funx()
#     ]
#
# done, pending = asyncio.run(asyncio.wait(task_list))
# print(done)


import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):

    time.sleep(1)
    print(value)
    return 123


pool = ThreadPoolExecutor(max_workers=5)

for i in range(10):

    fut = pool.submit(func, i)
    print(fut)


