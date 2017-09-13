#!env python3
# -*- coding: utf-8 -*-


import collections

from random import choice
from pprint import pprint

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]


def main():
    '''Some examples of usage'''


    print('-' * 80)
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    print('-' * 80)

    deck = FrenchDeck()
    print(len(deck))
    print('-' * 80)

    print(deck[0])
    print(deck[-1])
    print('-' * 80)

    print("Random sample")
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print(choice(deck))
    print('-' * 80)

    print("Take advantage of [] in __getitem__")
    pprint(deck[:3])
    pprint(deck[12::13])
    print('-' * 80)

    for card in deck:
        print(card)

    print("Reversed now")

    for card in reversed(deck):
        print(card)


    print('-' * 80)
    print("Pertinence")
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)

    print('-' * 80)
    print("Sorting")
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)

    print('-' * 80)

if __name__ == '__main__':
    main()
