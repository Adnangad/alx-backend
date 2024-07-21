import csv
import math
from typing import List, Tuple


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
        Returns pages
        """
        def index_range(page: int, page_size: int) -> Tuple[int, int]:
            """
            Args:
            page: the page number
            page_size: the total number of items in the page
            """
            start: int = (page - 1) * page_size
            end: int = start + page_size
            return(start, end)
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise AssertionError("Both page and page_size must be an integer")
        if page <= 0 or page_size<= 0:
            raise AssertionError("Both page and page_siz must be > 0")
        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]
