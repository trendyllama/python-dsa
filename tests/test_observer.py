"""
test_observer.py is a test file for the observer pattern.
"""

from src.design_patterns.observer import AppObserver, AppUser, Message


def test_observer():
    """
    Test the observer pattern. By resgistering multiple users to an observer,
    we can notify all users of a new message.
    """
    observer = AppObserver("observer")

    observer.subscribe(AppUser("user1"))
    observer.subscribe(AppUser("user2"))
    observer.subscribe(AppUser("user3"))

    observer.notify(Message("A new feature was just released!"))
