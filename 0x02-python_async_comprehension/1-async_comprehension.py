#!/usr/bin/env python3
""" Lorem ipsum dolor sit amet, consectetur adipiscing elit """

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Lorem ipsum dolor sit amet, consectetur adipiscing elit """

    return [i async for i in async_generator()]
