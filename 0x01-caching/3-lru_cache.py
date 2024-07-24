#!/usr/bin/env python3

"""LIFO Caching"""
from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """This defines a LIFO  caching class"""

    def __init__(self):
        """
        This method initializes the class with the
        contents of the super class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        This method adds a key-value pair to the cache_data
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)

            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f'DISCARD: {first_key}')
                del self.cache_data[first_key]

    def get(self, key):
        """
        This method takes in a 'key' argument and returns
        a the value associated by the provided 'key'
        """
        if not key or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
