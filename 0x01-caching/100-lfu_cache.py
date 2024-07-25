from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize the LFUCache
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.access_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.access_order.move_to_end(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = []
                for k, freq in self.frequency.items():
                    if freq == min_freq:
                        lfu_keys.append(k)

                if len(lfu_keys) > 1:
                    for k in self.access_order:
                        if k in lfu_keys:
                            evict_key = k
                            break
                else:
                    evict_key = lfu_keys[0]

                del self.cache_data[evict_key]
                del self.frequency[evict_key]
                self.access_order.pop(evict_key)
                print(f"DISCARD: {evict_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.access_order[key] = item

    def get(self, key):
        """ Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.access_order.move_to_end(key)
        return self.cache_data[key]
