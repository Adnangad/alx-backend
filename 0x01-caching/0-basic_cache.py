#!/usr/bin/python3
""" Basic cache system """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
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

    def get(self, key):
        """ Retreives a value from a dict """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
