"""
- helper functions for sorted tale
"""

import csv
from pathlib import Path


def load_books(filename: Path) -> list[str]:
    """
    This code loads the current book
    shelf data from the csv file
    """

    bookshelf = []

    with open(filename, "r", encoding="utf-8") as file:
        shelf = csv.DictReader(file)
        for book in shelf:
            # add your code here
            book["author_lower"] = book["author"].lower()
            book["title_lower"] = book["title"].lower()
            bookshelf.append(book)

    return bookshelf
