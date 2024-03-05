#1
import math

def multiply_numbers(numbers):
    # Use math.prod() to multiply all numbers in the list
    result = math.prod(numbers)
    return result

# Example usage
numbers = [1, 2, 3, 4, 5]
result = multiply_numbers(numbers)
print("List:", numbers)
print("Result of multiplying all numbers:", result)


