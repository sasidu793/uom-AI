def largest_prime_factor(n):
    """Returns the largest prime factor of the given number n."""
    factor = 2
    while factor * factor <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
    return n

print(largest_prime_factor(600851475143))