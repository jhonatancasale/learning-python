# -*- coding: utf-8 -*-

def main():
    '''A couple of print examples'''

    print('this is a test')
    print('this is a' + ' ' + 'test' )
    print('this is a', 'test' )
    a, b = 'this is a', 'test'
    print(f'{a} {b}')


    # Arbitrary values
    numbers = tuple(range(10))

    # Tuple style
    print(numbers)

    # Numbers style
    print(*numbers)

    # One by line
    print(*numbers, sep='\n')

    # Works with list too
    print(*list(range(10)))


if __name__ == '__main__':
    main()
