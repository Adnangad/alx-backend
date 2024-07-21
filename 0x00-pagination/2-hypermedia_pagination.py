#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict, Any
"""
Contains a module
"""


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Args:
        page: page number
        page_size: size of contents in page or page limit
        """
        start: int = (page - 1) * page_size
        end: int = start + page_size
        return(start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
        page: page number
        page_size: size of contents in page or page limit
        Returns:
        list of lists or empty list if page_size is out of range
        """
        assert type(page_size) == int and type(page) == int
        assert page > 0 and page_size > 0
        data = self.dataset()
        start, end = self.index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Args:
        page: page number
        page_size: size of contents in page or page limit
        """
        data: List[List] = self.get_page(page, page_size)
        total_pages: int = math.ceil(len(self.dataset()) / page_size)
        return {
                'page_size': page,
                'page': page,
                'data': data,
                'next_page': page + 1 if page < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
