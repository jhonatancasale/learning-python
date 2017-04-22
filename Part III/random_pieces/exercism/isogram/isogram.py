def is_isogram(string):
    """
    Determine if a word or phrase is an isogram. An isogram (also known as a
    "nonpattern word") is a word or phrase without a repeating letter.

    Examples:

    is_isogram(lumberjacks) -> True
    is_isogram(background) -> True
    is_isogram(downstream) -> True
    is_isogram(isograms) -> False
    """


    import re
    d = dict()
    parsed_string = "".join(re.split("[ \-]", string.lower()))
    for c in parsed_string:
        d[c] = d.get(c, 0) + 1
    return len(d) == len(parsed_string)
