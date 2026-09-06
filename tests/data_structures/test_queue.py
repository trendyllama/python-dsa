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


@pytest.mark.parametrize("value", list(range(1000)))
def test_multiple_dequeue(queue: Queue, value: int):
    for i in range(value):
        queue.enqueue(i)
        assert queue.size == i + 1
        assert queue.head is not None
        assert queue.head.value == 0
        assert queue.tail is not None
        assert queue.tail.value == i

    for i in range(value):
        queue.dequeue()
        assert queue.size == value - i - 1

    assert queue.size == 0
    assert queue.is_empty
    assert queue.head is None
    assert queue.tail is None
