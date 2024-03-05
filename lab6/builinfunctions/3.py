#3
def is_palindrome(string):
    # Reverse the string using slicing
    reversed_string = string[::-1]
    # Check if the original string is equal to its reverse
    return string == reversed_string

# Example usage
string = "radar"
result = is_palindrome(string)
if result:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")

