#!/usr/bin/env python3
'''BasicCache module'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''BasicCache class'''

    def put(self, key, item):
        '''Add and item in the cache'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Get an item by key'''
        if key is not None:
            return self.cache_data.get(key)
        return None
