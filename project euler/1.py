def sum_of_multiples(limit):
    """Returns the sum of all multiples of 3 or 5 below the given limit."""
    return sum(x for x in range(limit) if x % 3 == 0 or x % 5 == 0)
print(sum_of_multiples(1000))