#!/usr/bin/env python3
'''LFUCache module'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''LFUCache class'''

    def __init__(self):
        '''Initializw LFUCache'''
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        '''Add an item in the cache'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1

        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_least_frequent()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        '''Get an item by key'''
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None

    def remove_least_frequent(self):
        '''Remove the least frequent items'''
        items_to_discard = []
        min_freq_items = [
                key for key, freq in self.frequency.items()
                if freq == self.min_frequency]

        if min_freq_items:
            for key in self.cache_data.keys():
                if key not in min_freq_items:
                    items_to_discard.append(key)

            for key in min_freq_items:
                if key in self.cache_data:
                    del self.cache_data[key]
                    del self.frequency[key]
            print("DISCARD:", ', '.join(items_to_discard))
        else:
            mru_key = next(iter(self.cache_data))
            del self.cache_data[mru_key]
            del self.frequency[mru_key]
            print("DISCARD:", mru_key)
