import pytest

from src.data_structures.stack import Stack


@pytest.fixture
def stack():
    return Stack()

def test_push(stack):
    for i in range(1, 200):
        stack.push(i)
        assert stack.peek() == i

def test_pop(stack):
    for i in range(1, 200):
        stack.push(i)

    assert stack.size == 199

    for i in range(1, 199):
        stack.pop()
        assert stack.peek() == 199 - i

