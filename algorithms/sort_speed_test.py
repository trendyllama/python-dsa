import random
import time
from bubble_sort import bubble_sort
from elegant_quick_sort import quick_sort

nums = random.sample(range(1, 10000), 800)
# if multithreading, nums would need to be inside each functions local scope


s = time.time()
bubble_sort(nums)
elapsed = time.time() - s
print(f"Bubble sort took {elapsed} seconds")

s = time.time()
quick_sort(nums)
elapsed = time.time() - s
print(f"Quick sort took {elapsed} seconds")
