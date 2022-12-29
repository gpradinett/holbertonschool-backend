#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    class LRUCache that
    inherits from BaseCaching
    """
    def __init__(self):
        """
        method initialized
        """
        super().__init__()
        self.queued_item = deque()
        self.lru_item = []

    def put(self, key, item):
        """
        modify cache data
        Args: key: of the dict
             item: value of the key
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru_item.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    del self.cache_data[self.lru_item[0]]
                    print("DISCARD:", self.lru_item[0])
                    self.lru_item.pop(0)
                self.cache_data[key] = item
            self.lru_item.append(key)

    def get(self, key):
        """
        modify cache data
        Args: key: of the dict
        Return: value of the key
        """
        if key in self.cache_data:
            self.lru_item.remove(key)
            self.lru_item.append(key)
            return self.cache_data.get(key)
        else:
            return None
