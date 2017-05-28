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
# Create date Sat 27 May 20:59:30 -03 2017
'''

def sequential_search(t: list, elem: object) -> object:
    """
    Perform a sequential search for `elem` in `t` iterable. Return the index
    position of `elem` if `t` contains this element. -1 otherwise
    """


    try:
        return t.index(elem)
    except ValueError:
        return -1


def main():
    """
    Some test cases ...
    """

    t = [i * 2 for i in range(10)]
    assert(sequential_search(t, 4) == 2)
    assert(sequential_search(t, -4) == -1)

    assert(sequential_search([], 4) == -1)

if __name__ == '__main__':
    main()
