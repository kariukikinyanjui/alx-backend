#!/usr/bin/env python3
'''LIFOCache module'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFOCache class'''

    def __init__(self):
        '''Initialize LIFOCache'''
        super().__init__()

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is not None:
            return self.cache_data.get(key)
        return None
