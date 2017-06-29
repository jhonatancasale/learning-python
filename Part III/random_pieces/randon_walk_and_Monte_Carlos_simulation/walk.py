#!env python3
# -*- coding: utf-8 -*-

'''Perform Monte Carlo simulation'''

from random import choice

def random_walk(n):
    """Return cordinates after 'n' block random walk."""

    x, y = 0, 0
    for i in range(n):
        (dx, dy) = choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


def main():
    '''Perform Monte Carlo simulation'''


    number_of_walks = 20000

    for walk_length in range(1, 31):
        no_transport = 0 # Number of walks 4 or fewer blocks from home
        for i in range(number_of_walks):
            (x, y) = random_walk(walk_length)
            distance = abs(x) + abs(y)
            if distance <= 4:
                no_transport += 1
        no_transport_percentage = float(no_transport) / number_of_walks
        print('Walk size: {:2} / % of no transport: {}'.format(
            walk_length, 100 * no_transport_percentage)
        )


if __name__ == '__main__':
    main()
