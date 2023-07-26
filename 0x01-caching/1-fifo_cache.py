#!/usr/bin/env python3
"""Base cache algorithm"""



BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A class for FIFO caching"""

    def __init__(self):
        """Initialization function"""
        super().__init__()

    def put(self, key, item) -> None:
        """set a caching value"""
        if key is not None and item is not None:
            if len(self.cache_data) > (BaseCaching.MAX_ITEMS - 1):
                self.cache_data[key] = item
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD: {}".format(first_key))
            else:
                self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
        return None
