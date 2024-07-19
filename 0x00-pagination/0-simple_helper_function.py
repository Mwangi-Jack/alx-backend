#!/usr/bin/env python3
"""Simple pagination helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    This function takes in two integer arguments
    'page' and 'page_size' and returns a tuple of size
    two containing a start inde and an end index corresponding to the range
    of indexes to return
    """

    if page - 1 == 0:
        return (0, page_size)

    start = (page - 1 ) * page_size
    end = page * page_size
    return (start , end)
