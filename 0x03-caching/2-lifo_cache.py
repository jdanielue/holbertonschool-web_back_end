#!/usr/bin/python3
""" Sed ut perspiciatis unde omnis iste natusg  """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus  """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.LIFO = []

    def put(self, key, item):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.LIFO.remove(key)
                else:
                    del self.cache_data[self.LIFO[self.MAX_ITEMS - 1]]
                    discarded = self.LIFO.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", discarded)

            self.cache_data[key] = item
            self.LIFO.append(key)

    def get(self, key):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key in self.cache_data:
            return self.cache_data[key]
        return None
