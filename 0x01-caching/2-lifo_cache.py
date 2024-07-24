#!/usr/bin/evn python3

"""LIFO Caching"""

from more_itertools import value_chain


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """This defines a LIFO  caching class"""

    def __init__(self):
        """
        This method initializes the class with the
        contents of the super class
        """
        super().__init__()


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
                    last_item_key = list(self.cache_data.keys())[cache_length - 1]
                    print(f'DISCARD: {last_item_key}')
                    del self.cache_data[last_item_key]
                self.cache_data[key] = item

    def get(self, key):
        """
        This method takes in a 'key' argument and returns
        a the value associated by the provided 'key'
        """
        if not key or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
