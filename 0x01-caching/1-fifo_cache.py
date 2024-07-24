#!/usr/bin/env python3

"""FIFO Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """This class inherits from BaseCaching"""

    def __init__(self):
        """
        This method initializes the class with an inherited
        super class 'BaseCaching'
        """
        super().__init__()

    def put(self, key, item):
        """
        This method adds a key-value pair to the cache_data
        """

        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                first_key = list(self.cache_data.keys())[0]

                print(f'DISCARD {first_key}')
                del self.cache_data[first_key]

    def get(self, key):
        """
        This method takes in a 'key' argument and returns
        a the value associated by the provided 'key'
        """
        if not key or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
