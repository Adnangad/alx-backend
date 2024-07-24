#!/usr/bin/python3
""" FIFO cache system """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching
    """
    def __init__(self):
        """ Initializes attributes/params """
        super().__init__()

    def put(self, key, item):
        """ Adds a key value pair to a dict. """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        count = len(self.cache_data)
        if count > BaseCaching.MAX_ITEMS:
            x = 0
            for key in self.cache_data:
                x = x + 1
                if x == 1:
                    del self.cache_data[key]
                    print(f"DISCARD: {key}")
                    break

    def get(self, key):
        """ Retreives a value from a dict """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
