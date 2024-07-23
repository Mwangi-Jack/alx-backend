#!/usr/bin/env python3

"""Basic Cache that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    """The BasicCache class"""
    def __init__(self):
        """
        This method initialized the BasicCache class
        by calling the super class
        """
        super().__init__()


    def put(self, key, item):
        """
        This method adds a key-value pair to the cache_data
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        This method takes in a 'key' argument and returns
        a the value associated by the provided 'key'
        """
        if not key or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
