#!/usr/bin/env python3
'''LRUCache module'''
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRUCache class'''

    def __init__(self):
        '''Initialize LRUCache'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''Get an item by key'''
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
