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
import threading
import os


def task1():
    print("Task 1 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 1: {}".format(os.getpid()))


def task2():
    print("Task 2 assigned to thread: {}".format(threading.current_thread().name))
    print("ID of process running task 2: {}".format(os.getpid()))


async def tasks_example() -> None:
    task1_thread = asyncio.to_thread(task1)
    task2_thread = asyncio.to_thread(task2)

    res1, res2 = await asyncio.gather(task1_thread, task2_thread)

    print("Task 1 result: {}".format(res1))
    print("Task 2 result: {}".format(res2))


if __name__ == "__main__":
    # print ID of current process
    print("ID of process running main program: {}".format(os.getpid()))

    # print name of main thread
    print("Main thread name: {}".format(threading.current_thread().name))

    # creating threads
    t1 = threading.Thread(target=task1, name="t1")
    t2 = threading.Thread(target=task2, name="t2")

    # starting threads
    t1.start()
    t2.start()

    # wait until all threads finish
    t1.join()
    t2.join()
