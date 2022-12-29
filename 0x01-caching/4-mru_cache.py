#!/usr/bin/python3

"""
class MRUCache that inherits from BaseCaching and is a caching system
"""

from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache define MRU algorithm to use cache
    To use:
    >>> my_cache = BasicCache()
    >>> my_cache.print_cache()
    Current cache:
    >>> my_cache.put("A", "Hello")
    >>> my_cache.print_cache()
    A: Hello
    Ex:
    >>> my_cache.print_cache()
    Current cache:
    A: Hello
    B: World
    C: Holberton
    D: School
    >>> print(my_cache.get("B"))
    World
    DISCARD: B
    """

    def __init__(self):
        """
        Initialize
        """
        self.queued_item = deque()
        self.lru_item = []
        super().__init__()

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
                    del self.cache_data[self.lru_item[-1]]
                    print("DISCARD:", self.lru_item[-1])
                    self.lru_item.pop(-1)
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
