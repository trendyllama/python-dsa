from src.data_structures.queue import Queue


def test_enqueue():
    queue = Queue()

    for i in range(1, 20):
        queue.enqueue(i)
        assert queue.peek() == 1


def test_dequeue():
    queue = Queue()

    for i in range(1, 20):
        queue.enqueue(i)

    for i in range(1, 19):
        assert queue.peek() == i
        queue.dequeue()
