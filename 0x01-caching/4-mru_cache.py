#!/usr/bin/env python3

"""Most Recently Used (MRU) Caching"""

from collections import OrderedDict

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    This class defines the methods and attributes of the
    MRUCache class
    """

    def __init__(self):
        """
        This method initializes the MRUCache class with
        attributes from the super class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        This method adds a key-value pair to the cache_data
        """

        if key and item:
            if self.cache_data.get(key):
                self.cache_data[key] = item
            else:
                cache_length = len(self.cache_data.keys())
                if cache_length == BaseCaching.MAX_ITEMS:
                    last_item_key = next(reversed(self.cache_data))
                    print(f'DISCARD: {last_item_key}')
                    del self.cache_data[last_item_key]
                    # self.cache_data.pop(last_item_key)
                self.cache_data[key] = item

    def get(self, key):
        """
        This method takes in a 'key' argument and returns
        a the value associated by the provided 'key'
        """
        if not key or not self.cache_data.get(key):
            return None

        self.cache_data.move_to_end(key)

        return self.cache_data.get(key)
