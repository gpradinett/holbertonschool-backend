#!/usr/bin/python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        modify cache data
        Args: key: of the dict
        item: value of the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            keydel = list(self.cache_data.keys())[0]
            del self.cache_data[keydel]
            print("DISCARD: {}".format(keydel))

    def get(self, key):
        """
        modify cache data
        Args: key: of the dict
        Return: value of the key
        """
        if key is None or key not in self.cache_data:
            return None

        valuecache = self.cache_data.get(key)
        return valuecache
