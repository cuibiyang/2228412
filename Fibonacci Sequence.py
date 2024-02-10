def fibonacci_sequence(max_value):
    # Handle edge cases for 0 and negative inputs
    if max_value <= 0:
        if max_value == 0:
            return [0]
        else:
            return "Cannot generate Fibonacci sequence for negative input."
    
    # Initialize variables for Fibonacci sequence
    fib_sequence = [0, 1]
    next_fib = 1
    
    # Generate Fibonacci sequence using a while loop
    while next_fib <= max_value:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib <= max_value:
            fib_sequence.append(next_fib)
    
    return fib_sequence

# Example Test Cases
print(fibonacci_sequence(10))  # Output: Fibonacci sequence up to 10
print(fibonacci_sequence(1))   # Output: Fibonacci sequence up to 1
print(fibonacci_sequence(0))   # Output: [0]
print(fibonacci_sequence(-5))  # Output: Cannot generate Fibonacci sequence for negative input
