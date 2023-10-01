import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

# for book in bookshelf:
#   print(book['title'])

print(ord("a"))
# print(ord(""))
print(ord("A"))

def by_title_ascending(booka, bookb):
    if booka['title_lower'] > bookb['title_lower']:
        return True
    else:
        return False
    
def by_author_ascending(booka, bookb):
    if booka['author_lower'] > bookb['author_lower']:
        return True
    else:
        return False
    
def by_total_length(booka, bookb):
    if len(booka['title']) + len(booka['author']) > len(bookb['title']) + len(bookb['author']):
        return True
    else:
        return False
    
sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# for book in sort1:
#     print(book['title'])


bookshelf_v1 = bookshelf.copy()

sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

# for book in sort2:
#     print(book['author'])

bookshelf_v2 = bookshelf.copy()

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

for book in bookshelf_v2:
    print(book['author'])


long_bookshelf = utils.load_books('books_large.csv')

sorts.bubble_sort(long_bookshelf, by_total_length)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)