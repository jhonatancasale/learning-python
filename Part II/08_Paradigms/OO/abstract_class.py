#!env python3
# -*- coding: utf-8 -*-

import abc

class abstract_super_class(metaclass=abc.ABCMeta):
    '''Abstract Super class used in this examples'''


    @abc.abstractmethod
    def say_hello(self):
        '''Just say hello to the caller'''


class concrete_sub_class(abstract_super_class):

    def say_hello(self):
        print('Hi these!')


def main():
    '''
    - First, try to instantiate the abstract class and as expected, crash
    occurs
    - Second, instantiate the concrete_sub_class and run the `say_hello` method
    '''

    try:
        asc = abstract_super_class()
    except TypeError as te:
        print(te)

    concrete_sub_class().say_hello()


if __name__ == '__main__':
    main()
