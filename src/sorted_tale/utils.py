"""
- helper functions for sorted tale
"""

import csv
from pathlib import Path
from dataclasses import dataclass
import sqlite3


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


def load_books_to_db(filename: Path) -> None:
    """
    This code loads the current book shelf data from the csv file
    and saves it to the database

    """

    with (
        sqlite3.connect("books.db") as conn,
        open(filename, "r", encoding="utf-8") as file,
    ):
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                author_lower TEXT,
                title_lower TEXT
            )
            """
        )

        shelf = csv.DictReader(file)

        for book in shelf:
            cursor.execute(
                """
                INSERT INTO books (title, author, author_lower, title_lower)
                VALUES (?, ?, ?, ?)
                """,
                (
                    book["title"],
                    book["author"],
                    book["author"].lower(),
                    book["title"].lower(),
                ),
            )

        conn.commit()
