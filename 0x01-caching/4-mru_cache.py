#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the MRUCache
        """
        super().__init__()
        self.cache_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                mru_key, _ = self.cache_order.popitem(last=True)
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            self.cache_data[key] = item
            self.cache_order[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_order.move_to_end(key)
            return self.cache_data[key]
        return None
