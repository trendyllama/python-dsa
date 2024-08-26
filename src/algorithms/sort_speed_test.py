import random
import time
from .bubble_sort import bubble_sort
from .elegant_quick_sort import quick_sort

NUMS = [random.randint(1, 800) for _ in range(1000)]
# if multithreading, nums would need to be inside each functions local scope


s = time.time()
bubble_sort(NUMS)
elapsed = time.time() - s
print(f"Bubble sort took {elapsed} seconds")

s = time.time()
quick_sort(NUMS)
elapsed = time.time() - s
print(f"Quick sort took {elapsed} seconds")
