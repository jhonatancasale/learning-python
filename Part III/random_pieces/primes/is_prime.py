def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. 'False' otherwise"""

    if n == 1:
        return False    # 1 is not prime

    # If it's even and not 2, then it's not prime
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = floor(sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True
