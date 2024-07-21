#!/usr/bin/env python3
"""
This module contains a function that returns a typle.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
    page: the page number
    page_size: the total number of items in the page
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return(start, end)
