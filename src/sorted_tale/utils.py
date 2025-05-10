"""
- helper functions for sorted tale
"""

import csv
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Book:
    """
    This class represents a book

    """

    title: str
    author: str
    author_lower: str
    title_lower: str


def load_books(filename: Path) -> list[Book]:
    """
    This code loads the current book shelf data from the csv file

    """

    bookshelf: list[Book] = []

    with open(filename, "r", encoding="utf-8") as file:
        shelf = csv.DictReader(file)

    for book in shelf:
        # add your code here
        book_temp = Book(
            title=book["title"],
            author=book["author"],
            author_lower=book["author"].lower(),
            title_lower=book["title"].lower(),
        )
        bookshelf.append(book_temp)

    return bookshelf
