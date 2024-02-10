def compound_interest_calculator(P, r, n, t):
    # Handle edge cases
    if P <= 0 or r <= 0 or n <= 0 or t <= 0:
        return "Invalid input. Please provide positive values for all parameters."
    
    # Calculate compound interest
    A = P * (1 + r / n) ** (n * t)
    
    return A

# Example Test Cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Output: Calculate the amount.
print(compound_interest_calculator(500, 0.07, 4, 10))  # Output: Calculate the amount.
print(compound_interest_calculator(1500, 0.03, 6, 7))  # Output: Calculate the amount.
