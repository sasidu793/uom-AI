def even_fibonacci_sum(limit): 
    """Returns the sum of even Fibonacci numbers below the given limit.""" 
    a, b = 0, 1 
    total = 0 
    while b < limit: 
        if b % 2 == 0: 
            total += b 
        a, b = b, a + b 
    return total    
print(even_fibonacci_sum(4000000))