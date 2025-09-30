"""
test_observer.py is a test file for the observer pattern.
"""

import pytest

from src.design_patterns.observer import AppObserver, AppUser, Message


@pytest.fixture
def observer():
    return AppObserver("observer")


def test_observer(observer: AppObserver):
    """
    Test the observer pattern. By resgistering multiple users to an observer,
    we can notify all users of a new message.
    """

    observer.subscribe(AppUser("user1"))
    observer.subscribe(AppUser("user2"))
    observer.subscribe(AppUser("user3"))

    observer.notify(Message("A new feature was just released!"))
