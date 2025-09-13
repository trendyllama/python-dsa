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
import os
import threading


def _task1():
    print(f"Task 1 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 1: {os.getpid()}")


def _task2():
    print(f"Task 2 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 2: {os.getpid()}")


async def _tasks_example() -> None:
    task1_thread = asyncio.to_thread(_task1)
    task2_thread = asyncio.to_thread(_task2)

    res1, res2 = await asyncio.gather(task1_thread, task2_thread)

    print(f"Task 1 result: {res1}")
    print(f"Task 2 result: {res2}")


if __name__ == "__main__":
    # print ID of current process
    print(f"ID of process running main program: {os.getpid()}")

    # print name of main thread
    print(f"Main thread name: {threading.current_thread().name}")

    # creating threads
    t1 = threading.Thread(target=_task1, name="t1")
    t2 = threading.Thread(target=_task2, name="t2")

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
