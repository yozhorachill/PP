def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Use filter with a lambda function to filter prime numbers
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)
