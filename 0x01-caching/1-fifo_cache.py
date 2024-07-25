#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the FIFOCache
        """
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key, _ = self.cache_order.popitem(last=False)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.cache_order[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None:
            return None
        return self.cache_data.get(key)
