#!/usr/bin/python3

""" Sed ut perspiciatis unde omnis iste natus """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Sed ut perspiciatis unde omnis iste natus """

    def put(self, key, item):
        """ Put in cache """

        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get from cache """

        if key in self.cache_data:
            return self.cache_data[key]
        return None
