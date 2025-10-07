def is_palindrome(n):
    """Returns True if the given number n is a palindrome, False otherwise."""
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    """Finds the largest palindrome made from the product of two 3-digit numbers."""
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(largest_palindrome_product())