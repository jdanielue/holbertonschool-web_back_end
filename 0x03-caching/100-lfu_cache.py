#!/usr/bin/python3
""" Sed ut perspiciatis unde omnis iste natus   """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus    """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.LRU = []
        self.LRU_count = {}

    def put(self, key, item):
        """ Sed ut perspiciatis unde omnis iste natus """

        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.LRU.remove(key)
                else:
                    min = 99999
                    delete_key = 0
                    for key1, val in self.LRU_count.items():
                        if val < min:
                            min = val
                            delete_key = key1
                    del self.cache_data[delete_key]
                    del self.LRU_count[delete_key]
                    self.LRU.remove(delete_key)
                    print("DISCARD:", delete_key)

            self.cache_data[key] = item
            self.LRU.append(key)

            if self.LRU_count.get(key) is not None:
                self.LRU_count[key] += 1
            else:
                self.LRU_count[key] = 1

    def get(self, key):
        """ Sed ut perspiciatis unde omnis iste natus"""

        if key in self.cache_data:
            self.LRU_count[key] += 1
            return self.cache_data[key]

        return None
