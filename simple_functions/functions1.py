from functools import cache
from numpy import sqrt

__all__ = ['my_sum', 'factorial', 'pi']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n-1) if n else 1


def pi(terms=1):
    return 1./(2.*sqrt(2.)/9801.*rsum(terms))


@cache
def rsum(n):
    t = factorial(4*n)*(1103+26390*n)/(factorial(n)**4*396**(4*n))
    return t + rsum(n-1) if n else t
