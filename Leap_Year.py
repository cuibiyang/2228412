def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If it's a century year
        if year % 100 == 0:
            # Check if it's also divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Example Test Cases
print(is_leap_year(2020))  # Output: True
print(is_leap_year(1900))  # Output: False
print(is_leap_year(2000))  # Output: True
print(is_leap_year(2019))  # Output: False
