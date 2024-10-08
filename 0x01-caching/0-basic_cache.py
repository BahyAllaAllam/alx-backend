#!/usr/bin/python3
""" BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the BasicCache
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
