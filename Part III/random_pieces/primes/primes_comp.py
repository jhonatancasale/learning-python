#!env python3
# -*- coding: utf-8 -*-
'''Compare performance of some is_prime implementations'''

#from https://www.youtube.com/watch?v=2p3kwF04xcA


from time import time
from math import floor, sqrt
from sympy import isprime

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. 'False' otherwise"""

    if n == 1:
        return False    # 1 is not prime

    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. 'False' otherwise"""

    if n == 1:
        return False    # 1 is not prime

    max_divisor = floor(sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. 'False' otherwise"""

    if n == 1:
        return False    # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = floor(sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True


def main():
    '''Compare performance of some is_prime implementations'''

    prime_functions = [
        is_prime_v1,
        is_prime_v2,
        is_prime_v3,
        isprime
    ]

    for f in prime_functions:
        t0 = time()
        for n in range(1, 100000):
            f(n)
        t1 = time()
        print("Time required: {}".format(t1 - t0))


if __name__ == '__main__':
    main()
