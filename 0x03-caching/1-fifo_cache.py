#!/usr/bin/python3
""" Sed ut perspiciatis unde omnis iste natus """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus """

    def __init__(self):
        """ Sed ut perspiciatis unde omnis iste natus """

        super().__init__()
        self.FIFO = []

    def put(self, key, item):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded = self.FIFO.pop(0)
                del self.cache_data[discarded]
                print("DISCARD:", discarded)

            self.cache_data[key] = item
            self.FIFO.append(key)

    def get(self, key):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key in self.cache_data:
            return self.cache_data[key]
        return None
