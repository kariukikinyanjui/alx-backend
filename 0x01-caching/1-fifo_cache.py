#!/usr/bin/env python3
'''FIFOCache module'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache class'''

    def __init__(self):
        '''Initialize FIFOCache'''
        super().__init__()

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is not None:
            return self.cache_data.get(key)
        return None
