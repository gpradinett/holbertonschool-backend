#!/usr/bin/python3
"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache define a intro to use cache
    To use:
    >>> my_cache = BasicCache()
    >>> my_cache.print_cache()
    Current cache:
    >>> my_cache.put("A", "Hello")
    >>> my_cache.print_cache()
    A: Hello
    >>> print(my_cache.get("A"))
    Hello
    """
    def put(self, key, item):
        """
        modify cache data
        Args: key: of the dict
        item: value of the key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        modify cache data
        Args: key: of the dict
        Return: value of the key
        """
        if key is None or key not in self.cache_data:
            return None
        valuecache = self.cache_data.get(key)
        return (valuecache)
