import threading
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


_executor = ThreadPoolExecutor()

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     r = yield from asyncio.sleep(1)
#     print("Hello again!")


async def hello():
    print("Hello world!")
    # await asyncio.sleep(1)
    r = await loop.run_in_executor(_executor, t)  # 需要给予一个线程来启动
    print("Hello again!")


def t():
    time.sleep(1)
    print("!!!")


loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
