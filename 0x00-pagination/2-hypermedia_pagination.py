#!/usr/bin/env python3
"""Simple Pagination"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    This function takes in two integer arguments
    'page' and 'page_size' and returns a tuple of size
    two containing a start inde and an end index corresponding to the range
    of indexes to return
    """

    if page - 1 == 0:
        return (0, page_size)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding='utf-8') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        This method takes two integer arguments 'page' and 'page_size'
        with default values 1 and 10  and returns a the correct list of rows
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        self.dataset()
        indexes = index_range(page, page_size)

        return [data for data in self.__dataset[indexes[0]: indexes[1]]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        This method takes two integer arguments 'page' and 'page_size'
        with default values 1 and 10 and returns a dictionary containing
        pagination information.
        """

        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': total_pages}
