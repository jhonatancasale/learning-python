#!env python3
# -*- coding: utf-8 -*-

'''
#
# Create date Wed Aug  9 02:26:33 -03 2017
'''

def foo() -> None:
    print('foo')


def bar() -> None:
    print('bar')


def main():
    '''
    Example of usage `globals` to call functions from `strings`
    '''

    for function in ('foo', 'bar'):
        globals()[function]()


if __name__ == '__main__':
    main()
