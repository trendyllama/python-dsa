from src.data_structures.stack import Stack


class TestStack:
    def test_push(self):
        stack = Stack()

        for i in range(1, 200):
            stack.push(i)
            assert stack.peek() == i

    # def test_pop(self):
    #     stack = Stack()

    #     for i in range(1, 200):
    #         stack.push(i)

    #     for i in range(1, 200):
    #         assert stack.pop() == 200 - i

    def test_print_items(self):
        stack = Stack()

        for num in range(10):
            stack.push(num)

        stack.print()

    def test_iter(self):
        stack = Stack()

        for num in range(10):
            stack.push(num)

        for i in range(len(stack)):
            assert i == stack.pop()
