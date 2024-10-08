#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the LRUCache
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
                lru_key, _ = self.cache_order.popitem(last=False)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

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
