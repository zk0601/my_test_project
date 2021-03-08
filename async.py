# -*- coding: utf-8 -*-
import time
import asyncio


async def func1(num):
    print('1')
    m = await func2(num)
    # await asyncio.sleep(2)
    # m = num * 2
    print(m)
    return m


async def func2(num):
    # time.sleep(2)
    await asyncio.sleep(2)
    return num * 2


async def func3():
    # a = await func1(3)
    # b = await func1(4)
    # c = await func1(5)
    await asyncio.gather(func1(3), func1(4), func1(5))
    # print(a+b+c)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(func3())
    loop.close()
