# -*- coding: utf-8 -*-

def main():
    '''
    Samples example to `abs` builtin

    from: https://docs.python.org/3/library/functions.html#abs
    Return the absolute value of a number. The argument may be an integer or a
    floating point number. If the argument is a complex number, its magnitude is
    returned.
    '''

    print(abs(12))
    print(abs(-12))

    print(abs(12.3))
    print(abs(-12.3))

    print(abs(3+3j))

if __name__ == '__main__':
    main()
