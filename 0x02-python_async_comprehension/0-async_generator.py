#!/usr/bin/env python3

""" Lorem ipsum dolor sit amet, consectetur adipiscing elit  """

from asyncio import sleep
from random import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit  """

    for _ in range(10):
        yield random()
        await sleep(1)
