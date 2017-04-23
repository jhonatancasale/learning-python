def distance(strand1, strand2):
    """
    The Hamming distance between two DNA is found by comparing two DNA strands
    and counting how many of the nucleotides are different from their
    equivalent in the other string.

    Example:
        distance(GAGCCTACTAACGGGAT, CATCGTAATGACGGCCT) -> 7
    """

    if len(strand1) != len(strand2):
        raise ValueError
    return sum([_ != __ for _, __ in zip(strand1, strand2)])
