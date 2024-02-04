from datetime import datetime

# Input dates in the format dd/mm/yyyy
date1_str = input("Enter the first date (dd/mm/yyyy): ")
date2_str = input("Enter the second date (dd/mm/yyyy): ")

# Parse the input dates
date_format = "%d/%m/%Y"
date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

# Calculate the time difference
time_difference = date2 - date1

# Extract the total hours from the time difference
total_hours = time_difference.total_seconds() / 3600

# Display the result
print(f"The total hours between {date1_str} and {date2_str} is {total_hours} hours.")
