def add(x, y):
    '''Add Funcition'''

    return x + y


def subtract(x, y):
    '''Subtract Funcition'''

    return x - y


def multiply(x, y):
    '''Multiply Funcition'''

    return x * y


def divide(x, y):
    '''Divide Funcition'''

    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
