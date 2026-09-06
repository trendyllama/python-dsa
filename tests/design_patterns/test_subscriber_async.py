import asyncio

from src.design_patterns.subscriber import Config


class FakeSubscriber:
    def __init__(self):
        self.received = []
        self._lock = asyncio.Lock()

    async def receive_diff(self, diff):
        async with self._lock:
            self.received.append(diff)


async def test_config_notifies_diff_subscribers():
    config = Config()
    subscriber = FakeSubscriber()

    await config.subscribe(subscriber)
    await config.put("feature_flag", True)
    await config.put("feature_flag", False)

    assert subscriber.received == [
        {"key": "feature_flag", "old": None, "new": True, "version": 1},
        {"key": "feature_flag", "old": True, "new": False, "version": 2},
    ]

    diffs = await config.get_diffs()
    assert diffs == subscriber.received


async def test_config_unsubscribe_stops_notifications():
    config = Config()
    subscriber = FakeSubscriber()

    await config.subscribe(subscriber)
    await config.put("mode", "dark")
    await config.unsubscribe(subscriber)
    await config.put("mode", "light")

    assert subscriber.received == [
        {"key": "mode", "old": None, "new": "dark", "version": 1},
    ]


async def test_concurrent_puts_create_ordered_versions():
    config = Config()
    subscriber = FakeSubscriber()

    await config.subscribe(subscriber)

    async def do_put(i):
        await config.put("concurrent", f"v{i}")

    await asyncio.gather(*(do_put(i) for i in range(5)))

    diffs = sorted(await config.get_diffs(), key=lambda d: d["version"])
    assert len(diffs) == 5
    assert [d["version"] for d in diffs] == [1, 2, 3, 4, 5]
