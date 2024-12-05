from src.data_structures.queue import Queue


class TestQueue:
    def test_enqueue(self):
        queue = Queue()

        for i in range(1, 20):
            queue.enqueue(i)
            assert queue.peek() == 1

    def test_dequeue(self):
        queue = Queue()

        for i in range(1, 20):
            queue.enqueue(i)

        for i in range(1, 20):
            queue.dequeue()
            assert queue.peek() == i
