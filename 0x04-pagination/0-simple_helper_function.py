#!/usr/bin/env python3
""" "Lorem ipsum dolor sit amet """


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Lorem ipsum dolor sit amet """
    return (((page - 1) * page_size), (page * page_size))
