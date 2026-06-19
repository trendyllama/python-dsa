

import asyncio
import datetime
from typing import Protocol, Any


class DiffSubscriber(Protocol):
    async def receive_diff(self, diff: dict[str, Any]) -> Any: ...


class Publisher(Protocol):
    async def subscribe(self, subscriber: DiffSubscriber) -> None: ...

    async def unsubscribe(self, subscriber: DiffSubscriber) -> None: ...


class Config[Index: int](Publisher):
    def __init__(self):
        self._data = {}
        self._diffs: dict[tuple[str, Index], dict[str, Any]] = {}
        self._subscribers: list[DiffSubscriber] = []
        self._lock = asyncio.Lock()

    async def snapshot(self):
        # Simulate taking a snapshot of the current configuration
        async with self._lock:
            return self._data.copy(), self._diffs.copy(), datetime.datetime.now()

    async def get(self, key):
        async with self._lock:
            return self._data.get(key, None)

    async def subscribe(self, subscriber: DiffSubscriber) -> None:
        async with self._lock:
            self._subscribers.append(subscriber)

    async def unsubscribe(self, subscriber: DiffSubscriber) -> None:
        async with self._lock:
            self._subscribers.remove(subscriber)

    async def _notify_diff_listeners(self, diff: dict[str, Any]) -> None:
        async with self._lock:
            subscribers = list(self._subscribers)

        for subscriber in subscribers:
            await subscriber.receive_diff(diff)

    async def put(self, key, value):
        async with self._lock:
            old_value = self._data.get(key, None)
            self._data[key] = value

            max_idx = max((idx for (_, idx) in self._diffs), default=0)
            diff = {
                "key": key,
                "old": old_value,
                "new": value,
                "version": max_idx + 1,
            }
            self._diffs[(key, diff["version"])] = diff

        await self._notify_diff_listeners(diff)

    async def get_diffs(self) -> list[dict[str, Any]]:
        async with self._lock:
            return list(self._diffs.values())
