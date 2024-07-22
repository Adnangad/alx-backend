#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """uses key pagination
        """
        assert index >= 0
        data = self.indexed_dataset()
        assert index <= len(data)
        keys = sorted(data.keys())
        count = 0
        cur_idx = index
        idx_data = []
        while count < page_size and cur_idx < len(keys):
                if cur_idx in data:
                        idx_data.append(data[cur_idx])
                        count = count + 1
                cur_idx = cur_idx + 1
        next_index = cur_idx if cur_idx < len(keys) else None
        return {
            'index': index,
            'data': idx_data,
            'page_size': page_size,
            'next_index': next_index
        }