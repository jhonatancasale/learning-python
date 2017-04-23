def word_count(phrase):
    """
    Given a phrase, count the occurrences of each word in that phrase.

    For example for the input `"olly olly in come free"`

    olly: 2
    in: 1
    come: 1
    free: 1
    """

    from collections import OrderedDict
    import re

    d = OrderedDict()
    t = re.compile('[^a-zA-Z0-9]').sub(' ', phrase).lower().split()
    for word in t:
        d[word] = t.count(word)
    return d
