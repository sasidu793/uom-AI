def Summation_of_Primes(n):
    """Returns the sum of all prime numbers below n."""
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n, i):
                sieve[j] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)
print(Summation_of_Primes(2000000))