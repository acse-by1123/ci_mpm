from functools import cache

__all__ = ['my_sum', "my_factorial"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def my_factorial(n):
    return n * my_factorial(n-1) if n else 1
