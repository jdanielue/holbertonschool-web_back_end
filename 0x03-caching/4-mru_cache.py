#!/usr/bin/python3
""" Sed ut perspiciatis unde omnis iste natus   """

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.MRU = []

    def put(self, key, item):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.MRU.remove(key)
                else:
                    del self.cache_data[self.MRU[self.MAX_ITEMS - 1]]
                    discarded = self.MRU.pop(self.MAX_ITEMS - 1)
                    print("DISCARD:", discarded)

            self.cache_data[key] = item
            self.MRU.append(key)

    def get(self, key):
        """ Sed ut perspiciatis unde omnis iste natuse """

        if key in self.cache_data:
            self.MRU.remove(key)
            self.MRU.append(key)
            return self.cache_data[key]

        return None
