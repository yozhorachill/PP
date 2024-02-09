#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

# Example usage:
grams_amount = 100
ounces_amount = grams_to_ounces(grams_amount)
print(f"{grams_amount} grams is equal to {ounces_amount:.2f} ounces.")


#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Считываем температуру в градусах Фаренгейта из ввода пользователя
fahrenheit_temperature = float(input("Введите температуру в градусах Фаренгейта: "))

# Преобразуем температуру из градусов Фаренгейта в градусы Цельсия, используя функцию
celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)

# Выводим эквивалентную температуру в градусах Цельсия
print(f"{fahrenheit_temperature} градусов Фаренгейта равно {celsius_temperature:.2f} градусам Цельсия.")


#3
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))
solve(35,94)


#4
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Example usage:
numbers_list = input("Enter a list of numbers separated by spaces: ").split()
numbers_list = [int(num) for num in numbers_list]

prime_numbers = filter_prime(numbers_list)
print("Prime numbers:", prime_numbers)


#5
from itertools import permutations

def print_permutations(input_string):
    
    permuted_strings = [''.join(p) for p in permutations(input_string)]
    
    print("All permutations of the string:")
    for permuted_string in permuted_strings:
        print(permuted_string)

# Example usage:
user_input = input("Enter a string: ")
print_permutations(user_input)
