#!/usr/bin/python3
""" LIFO cache system """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    def __init__(self):
        """ Initializes attributes/params """
        super().__init__()
        self.ls = []

    def put(self, key, item):
        """ Adds a key value pair to a dict. """
        if key is None or item is None:
            return
        self.ls.append(key)
        if key in self.cache_data:
            self.cache_data[key] = item
        self.cache_data[key] = item
        count = len(self.cache_data)
        if count > BaseCaching.MAX_ITEMS:
            keyz = self.ls[-2]
            del self.cache_data[keyz]
            print(f"DISCARD: {keyz}")

    def get(self, key):
        """ Retreives a value from a dict """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
