#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int]:
    """
    The function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular
    pagination parameters
    """
    start_index = page_size * (page - 1)
    end_index = start_index + page_size
    result = (start_index, end_index)

    return result


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
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        method named get_page that takes two integer arguments
        page with default value 1 and page_size with default value 10
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        result = index_range(page, page_size)
        start = int(result[0])
        end = int(result[1])

        return(self.dataset()[start: end])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """

        """
        record_dataset = self.get_page(page, page_size)
        page_dict = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(record_dataset),
            'page': page,
            'data': record_dataset,
            'next_page': page + 1 if (page + 1) <= page_dict else Nose,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': page_dict
        }
