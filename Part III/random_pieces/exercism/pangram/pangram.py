def is_pangram(string):
    """
    Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
    gramma, "every letter") is a sentence using every letter of the alphabet at
    least once.

    Example
    is_pangram("The quick brown fox jumps over the lazy dog.") -> True

    The alphabet used is ASCII, and case insensitive, from 'a' to 'z'
    inclusively.
    """


    import re
    letters = dict()
    parsed_string = "".join(re.split("[ _\-.]", string.lower()))
    for _ in parsed_string:
        if str.isalpha(_):
            letters[_] = letters.get(_, 0) + 1
    return len(letters) == 26 # 26 letters from 'a' to 'z'
