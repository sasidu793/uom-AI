def sum_of_squares(n):
    """Returns the sum of the squares of the first n natural numbers."""
    return sum(i * i for i in range(1, n + 1))

def square_of_sum(n):
    """Returns the square of the sum of the first n natural numbers."""
    total = sum(i for i in range(1, n + 1))
    return total * total

def difference(n):
    """Returns the difference between the square of the sum and the sum of the squares."""
    return square_of_sum(n) - sum_of_squares(n)

print(difference(100))
