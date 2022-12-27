#!/usr/bin/env python3
from typing import Tuple
"""
Simple helper function
"""


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size two containing a start index and an end
    index corresponding to the range of indexes to return in a list
    for those particular pagination parameters.
    """

    final_size = page * page_size
    start_size = final_size - page_size

    return (start_size, final_size)
