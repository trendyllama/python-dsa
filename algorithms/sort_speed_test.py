from algorithms.bubble_sort import bubble_sort
from algorithms.elegant_quick_sort import quick_sort
import time
import random

nums = random.sample(range(1, 1000), 800)
# if multithreading, nums would need to be inside each functions local scope


s = time.time()
bubble_sort(nums)
elapsed = time.time() - s
print("Bubble sort took {} seconds".format(elapsed))

s = time.time()
quick_sort(nums)
elapsed = time.time() - s
print("Quick sort took {} seconds".format(elapsed))
