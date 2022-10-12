#!/usr/bin/python3
""" Sed ut perspiciatis unde omnis iste natus   """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus   """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.LRU = []

    def put(self, key, item):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.LRU.remove(key)
                else:
                    del self.cache_data[self.LRU[0]]
                    discarded = self.LRU.pop(0)
                    print("DISCARD:", discarded)

            self.cache_data[key] = item
            self.LRU.append(key)

    def get(self, key):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key in self.cache_data:
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.cache_data[key]

        return None
