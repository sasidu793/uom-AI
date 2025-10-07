def seventh_prime():
    """Returns the 7th prime number."""
    count = 0
    num = 1
    while count < 7:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return num
print(seventh_prime())
