def case_counter(text):
    # Initialize counts for uppercase and lowercase letters
    upper_count = 0
    lower_count = 0
    
    # Iterate through each character in the string
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            upper_count += 1
        # Check if the character is a lowercase letter
        elif char.islower():
            lower_count += 1
    
    # Print the counts of uppercase and lowercase letters
    print("Uppercase count:", upper_count)
    print("Lowercase count:", lower_count)

# Example Test Cases
case_counter("Hello World!")  # Output: Uppercase count: 1, Lowercase count: 9
case_counter("PYTHON")  # Output: Uppercase count: 6, Lowercase count: 0
case_counter("python")  # Output: Uppercase count: 0, Lowercase count: 6
case_counter("1234!@#$")  # Output: Uppercase count: 0, Lowercase count: 0
