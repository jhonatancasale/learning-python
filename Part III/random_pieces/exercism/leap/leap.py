def is_leap_year(year):
    """
    A leap year in the Gregorian calendar occurs:
    on every year that is evenly divisible by 4
        except every year that is evenly divisible by 100
            unless the year is also evenly divisible by 400

    Example:
        is_leap_year(1997) -> False
        is_leap_year(1996) -> True
        is_leap_year(1900) -> False
        is_leap_year(2000) -> True
    """


    return (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0
