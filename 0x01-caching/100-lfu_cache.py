#!/usr/bin/env python3
"""Least Frequently Used (LFU) Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    This class LFUCache inherits from
    BaseCaching and is a caching system with LFU policy
    """
    def __init__(self):
        """This method initializes the LFUCache class"""
        super().__init__()
        self.cache_data = {}
        self.frequency_data = {}

    def put(self, key, item):
        """This method adds a key value pair to the cache_data"""

        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency_data[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    least_frequent_key = min(self.frequency_data,
                                             key=self.frequency_data.get)
                    print(f'DISCARD: {least_frequent_key}')

                    del self.cache_data[least_frequent_key]
                    del self.frequency_data[least_frequent_key]

                self.cache_data[key] = item
                self.frequency_data[key] = 1

    def get(self, key):
        """
        This method takes in an argument 'key' and returns
        an item associated with the provided 'key' while
        increasing its frequency
        """

        if key is None or key not in self.cache_data:
            return None

        self.frequency_data[key] += 1
        return self.cache_data[key]
