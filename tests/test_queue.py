import pytest

from src.data_structures.queue import Queue


@pytest.fixture
def queue() -> Queue:
    queue = Queue()

    return queue


def test_enqueue(queue: Queue):
    queue.enqueue(1)

    assert queue.head is not None
    assert queue.head.value == 1
    assert queue.head.next_node is None

    queue.enqueue(2)
    assert queue.head.value == 1
    assert queue.tail is not None
    assert queue.tail.value == 2
    assert queue.tail.next_node is not None
    assert queue.tail.next_node.value == 1


def test_dequeue(queue: Queue):
    queue.enqueue(1)
    queue.enqueue(2)

    queue.dequeue()
    assert queue.head is not None
    assert queue.tail is not None
    assert queue.head.value == 2
    assert queue.tail.value == 2
    assert queue.size == 1

    queue.dequeue()
    assert queue.head is None
    assert queue.tail is None
    assert queue.size == 0
    assert queue.is_empty


def test_multiple_dequeue(queue: Queue):
    for i in range(1, 10):
        queue.enqueue(i)
        assert queue.size == i
        assert queue.head is not None
        assert queue.head.value == 1
        assert queue.tail is not None
        assert queue.tail.value == i

    assert queue.size == 9
    assert queue.head is not None
    assert queue.head.value == 1
    assert queue.tail is not None
    assert queue.tail.value == 9

    for i in range(1, 10):
        queue.dequeue()
        assert queue.size == 9 - i

    assert queue.size == 0
    assert queue.is_empty
    assert queue.head is None
    assert queue.tail is None
