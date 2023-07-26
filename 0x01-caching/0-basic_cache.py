#!/usr/bin/env python3
"""Base cache algorithm"""


from typing import Union

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A class for basic caching"""

    def __init__(self):
        """Initialization function"""
        super().__init__()

    def put(self, key, item) -> None:
        """set a caching value"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            return self.cache_data.get(key)
        return None
