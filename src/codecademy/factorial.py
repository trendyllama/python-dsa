from functools import lru_cache

# recursive function for factorials

@lru_cache
def fact(n):
    '''
    Example:
    >>> fact(5)
    120
    >>> fact(3)
    6
    >>> fact(0)
    1
    >>> fact(10)
    3628800
    '''
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if n == 0:
        return 1
    else:
        return n * fact(n - 1)



def fact_itr(n):
    '''
    Example:
    >>> fact_itr(5)
    120
    >>> fact_itr(3)
    6
    >>> fact_itr(0)
    1
    >>> fact_itr(10)
    3628800
    '''
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
