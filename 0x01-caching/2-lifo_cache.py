#!/usr/bin/python3
"""

"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that
    inherits from BaseCaching
    """
    def __init__(self):
        """
        method initialized
        """
        super().__init__()

    def put(self, key, item):
        """

        """
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """

        """
        if key is None or key not in self.cache_data:
            return None

        valuecache = self.cache_data.get(key)
        return valuecache
