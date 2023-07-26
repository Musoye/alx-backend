#!/usr/bin/env python3
"""Base cache algorithm"""


from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
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
        if key and key is self.cache_data.keys():
            item = self.cahe_data.get(key)
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return item
        return None
