from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Define the format of the date strings
    date_format = '%dth %B'
    
    # Convert the date strings to datetime objects
    today = datetime.strptime(todays_date, date_format)
    scheduled = datetime.strptime(scheduled_date, date_format)
    
    # Compare the dates
    if today < scheduled:
        print("The scheduled date is yet to pass.")
    elif today > scheduled:
        print("The scheduled date has passed.")
    else:
        print("The scheduled date is today.")

# Example Test Cases
date_passed('26th March', '25th March')  # Output: The scheduled date has passed.
date_passed('26th March', '26th March')  # Output: The scheduled date is today.
date_passed('26th March', '27th March')  # Output: The scheduled date is yet to pass.
