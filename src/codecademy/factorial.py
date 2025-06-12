import time
from functools import lru_cache

# recursive function for factorials

@lru_cache
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


# print(fact(5))
# print(fact(3))

# iterative function for factorials


def fact_itr(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


s = time.time()
print(fact_itr(40))
e = time.time() - s
print(f"Iterative Factorial function took {e} seconds to run")

s = time.time()
print(fact(40))
e = time.time() - s
print(f"Recursive Factorial function took {e} seconds to run")