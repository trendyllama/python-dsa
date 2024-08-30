"""
- testing data structures and algos
"""

import unittest
import random
from src.data_structures.stack import Stack
from src.data_structures.queue import Queue
from src.data_structures.linked_list import LinkedList
from src.algorithms.elegant_quick_sort import quick_sort


class TestStack(unittest.TestCase):

    def test_push(self):

        stack = Stack()

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.peek(), 2)

        stack.pop()
        self.assertEqual(stack.peek(), 1)


class TestQuicksort(unittest.TestCase):

    def test_quicksort(self):

        self.assertEqual(quick_sort([3, 6, 2, 9]), [2, 3, 6, 9])

        RAND_LIST = [random.randint(1, 50) for _ in range(50)]

        self.assertEqual(quick_sort(RAND_LIST), list(set(sorted(RAND_LIST))))


class TestQueue(unittest.TestCase):

    def test_enqueue(self):

        queue = Queue()

        for i in range(1, 20):

            queue.enqueue(i)

        queue.print()


class TestLinkedList(unittest.TestCase):

    def test_linked_list(self):

        ll = LinkedList()

        for i in range(1, 11):

            ll.insert(i)

        for node in ll:
            print(node)
