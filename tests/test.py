"""
- testing data structures and algos
"""

import random

from src.algorithms.elegant_quick_sort import quick_sort


class TestQuicksort:
    def test_quicksort(self):
        assert quick_sort([3, 6, 2, 9]) == [2, 3, 6, 9]

        RAND_LIST = [random.randint(1, 50) for _ in range(50)]

        assert quick_sort(RAND_LIST) == list(set(sorted(RAND_LIST)))


# class TestLinkedList(unittest.TestCase):

#     def test_linked_list(self):

#         ll = LinkedList()

#         for i in range(1, 11):

#             # FIXME: does a node really need to be instantiated here?
#             ll.insert(Node(i))

#         for node in ll:
#             print(node)
