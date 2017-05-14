#!env python3
# -*- coding: utf-8 -*-

'''
# Author: Jhonatan Casale (jhc)
#
# Contact : jhonatan@jhonatancasale.com
#         : casale.jhon@gmail.com
#         : https://github.com/jhonatancasale
#         : https://twitter.com/jhonatancasale
#         : http://jhonatancasale.github.io/
#
# Create date Sat 13 May 20:54:54 -03 2017
'''

def sum_divs_interval(m: int, n: int) -> int:
    return -1 if m > n else sum(sum_divs(i) for i in range(m, n+1))


def sum_divs(m: int) -> int:
    return sum(i for i in range(1, m+1) if m % i == 0)


def main():
    '''
    '''

    m = int(input())
    n = int(input())

    print("Sum of divisors from {}, to {} is {}\n".format(
           m, n, sum_divs_interval(m, n)))


if __name__ == '__main__':
    main()
