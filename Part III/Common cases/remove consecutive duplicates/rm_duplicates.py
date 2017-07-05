# -*- coding: utf-8 -*-

from itertools import groupby

def rm_consec_letters(word):
    '''Return "word" without identical consecutive letters'''

    return ''.join(l for l, _ in groupby(word))


def rm_consec_letters_self_made(word):
    '''Return "word" without identical consecutive letters'''

    if len(word) < 2:
        return word
    return word[0] + ''.join(s for f, s in zip(word, word[1:]) if f != s)
