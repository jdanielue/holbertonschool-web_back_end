#!/usr/bin/python3
""" Lorem ipsum dolor sit amet
"""


class BaseCaching():
    """ Lorem ipsum dolor sit amet,
      - Lorem ipsum dolor sit amet
      - Lorem ipsum dolor sit amet
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Lorem ipsum dolor sit amet
        """
        self.cache_data = {}

    def print_cache(self):
        """ Lorem ipsum dolor sit amet
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Lorem ipsum dolor sit amet
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")
