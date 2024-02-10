def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    
    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    
    # If no divisor is found, the number is prime
    return True

# Example Test Cases
print(is_prime(11))  # Output: True
print(is_prime(4))   # Output: False
print(is_prime(2))   # Output: True
print(is_prime(1))   # Output: False
