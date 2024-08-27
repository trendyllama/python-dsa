import random
from timeit import timeit

# from src.algorithms.bubble_sort import bubble_sort
# from src.algorithms.elegant_quick_sort import quick_sort
from bubble_sort import bubble_sort
from elegant_quick_sort import quick_sort


NUMS = [random.randint(1, 800) for _ in range(1000)]
# if multithreading, nums would need to be inside each functions local scope


timeit(stmt="bubble_sort(NUMS)")
timeit(stmt="quick_sort(NUMS)")
