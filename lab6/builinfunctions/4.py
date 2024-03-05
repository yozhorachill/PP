#4
import time
import math

def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    return result

# Sample Input
number = 25100
milliseconds = 2123

# Calculate square root after delay
result = delayed_square_root(number, milliseconds)

# Sample Output
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")