#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the LIFOCache
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = self.cache_order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        self.cache_data[key] = item
        self.cache_order.append(key)

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None:
            return None
        return self.cache_data.get(key)
