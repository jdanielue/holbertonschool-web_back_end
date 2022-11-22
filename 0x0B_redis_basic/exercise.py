#!/usr/bin/env python3
""" Lorem ipsum dolor sit amet, consectetur """
from functools import wraps
import redis
from typing import Union, Optional, Callable
from uuid import uuid4, UUID


def count_calls(method: Callable) -> Callable:
    """ Lorem ipsum dolor sit amet """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Lorem ipsum dolor sit amet  """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """ Lorem ipsum dolor sit amet  """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ WLorem ipsum dolor sit amet  """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output

    return wrapper
