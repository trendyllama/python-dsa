from src.data_structures.queue import Queue


class TestQueue:
    def test_enqueue(self):
        queue = Queue()

        for i in range(1, 20):
            queue.enqueue(i)

        queue.print()
