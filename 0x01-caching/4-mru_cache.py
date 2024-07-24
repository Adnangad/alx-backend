#!/usr/bin/python3
""" MRU cache system """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
        if key in self.cache_data:
            self.ls.remove(key)
        self.ls.append(key)
        self.cache_data[key] = item
        count = len(self.cache_data)
        if count > BaseCaching.MAX_ITEMS:
            keyz = self.ls.pop(-2)
            del self.cache_data[keyz]
            print(f"DISCARD: {keyz}")

    def get(self, key):
        """ Retreives a value from a dict """
        if key is None or key not in self.cache_data:
            return None
        self.ls.remove(key)
        self.ls.append(key)
        return self.cache_data[key]
