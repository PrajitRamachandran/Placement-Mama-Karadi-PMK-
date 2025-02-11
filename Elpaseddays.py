from datetime import datetime

def elapsed_days(date1, date2):
    format_str = "%Y-%m-%d"
    d1 = datetime.strptime(date1, format_str)
    d2 = datetime.strptime(date2, format_str)
    return abs((d2 - d1).days)

# Input
date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

# Output
print(f"Elapsed days between {date1} and {date2}: {elapsed_days(date1, date2)}")
