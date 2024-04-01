#!/usr/bin/env python3
'''A function that takes two arguments'''


def index_range(page: int, page_size: int):
    '''
    Calculate the start and end indices for a given page and page size

    Args:
        page(int): The page number (1-indexed)
        page_size(int): The number of items per page

    Returns:
        tuple[int, int]: A tuple containing the start and end indices for
        the given page
    '''

    start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return start_index, end_index
