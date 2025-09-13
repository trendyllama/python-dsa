"""
- Multithreading is when you can execute multiple locally contained processes simultaneously.
- Different functions (processes) are defined in their own scope before the main thread.
- In python, there is not true multithreading but simulated multithreading via the threading module.
- To calculate time.

```python
import time

s = time.perf_counter()
elapsed = time.perf_counter() - s
print("Executed in: " + str(elapsed) + " seconds")
```

"""

import asyncio
import logging
import os
import threading

logger = logging.getLogger(__name__)


def _task1():
    logger.info("Task 1 assigned to thread: %s", threading.current_thread().name)
    logger.info("ID of process running task 1: %s", os.getpid())


def _task2():
    logger.info("Task 2 assigned to thread: %s", threading.current_thread().name)
    logger.info("ID of process running task 2: %s", os.getpid())


async def _tasks_example() -> None:
    task1_thread = asyncio.to_thread(_task1)
    task2_thread = asyncio.to_thread(_task2)

    res1, res2 = await asyncio.gather(task1_thread, task2_thread)

    logger.info("Task 1 result: %s", res1)
    logger.info("Task 2 result: %s", res2)


if __name__ == "__main__":
    # logger.info ID of current process
    logger.info("ID of process running main program: %s", os.getpid())

    # logger.info name of main thread
    logger.info("Main thread name: %s", threading.current_thread().name)

    # creating threads
    t1 = threading.Thread(target=_task1, name="t1")
    t2 = threading.Thread(target=_task2, name="t2")

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
