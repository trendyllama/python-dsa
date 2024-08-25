
import unittest
from src.data_structures.stack import Stack
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

        self.assertEqual(quick_sort([3,6,2,9]), [2,3,6,9])