from src.data_structures.stack import Stack


class TestStack:
    def test_push(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)

        assert stack.peek() == 2

        stack.pop()

        assert stack.peek() == 1

    def test_print_items(self):
        stack = Stack()

        for num in range(10):
            stack.push(num)

        stack.print()
