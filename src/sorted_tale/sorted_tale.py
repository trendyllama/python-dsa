"""
- main module for stored tale project
- uses functions from sorts.py and utils.py
"""

import logging
from operator import gt
from pathlib import Path

from src.algorithms.quick_sort import quicksort

from .sorts import bubble_sort
from .utils import load_books

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    bookshelf = load_books(Path("src/sorted_tale/books_small.csv"))

    logger.info(ord("a"))

    logger.info(ord("A"))

    def by_title_ascending(booka, bookb) -> bool:
        return gt(booka["title_lower"], bookb["title_lower"])

    def by_author_ascending(booka, bookb) -> bool:
        return gt(booka["author_lower"], bookb["author_lower"])

    def by_total_length(booka, bookb) -> bool:
        return gt(
            len(booka["title"]) + len(booka["author"]),
            len(bookb["title"]) + len(bookb["author"]),
        )

    sort1 = bubble_sort(bookshelf, by_title_ascending)

    bookshelf_v1 = bookshelf.copy()

    sort2 = bubble_sort(bookshelf_v1, by_author_ascending)

    bookshelf_v2 = bookshelf.copy()

    quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

    for book in bookshelf_v2:
        logger.info(book["author"])

    long_bookshelf = load_books(Path("books_large.csv"))

    bubble_sort(long_bookshelf, by_total_length)

    quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)
