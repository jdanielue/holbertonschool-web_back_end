#!/usr/bin/env python3

""" Lorem ipsum dolor sit amet, consectetur adipiscing elit """

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit  """

    start = time()
    await gather(async_comprehension(),
                 async_comprehension(),
                 async_comprehension(),
                 async_comprehension())

    end = time()
    return end - start
