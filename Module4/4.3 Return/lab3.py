def is_year_leap(year):
    # Check if the year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    # Check if the month is valid
    if month < 1 or month > 12:
        return "Invalid month"

    # Check if the year is a leap year
    leap = is_year_leap(year)

    # Days in each month
    days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days_in_month[month - 1]

def day_of_year(year, month, day):
    # Check if the year is valid
    if year < 1:
        return "Invalid year"

    # Check if the month is valid
    if month < 1 or month > 12:
        return "Invalid month"

    # Check if the day is valid
    days_in_this_month = days_in_month(year, month)
    if day < 1 or day > days_in_this_month:
        return "Invalid day"

    # Calculate the day of the year
    day_of_year = sum(days_in_month(year, m) for m in range(1, month)) + day

    return day_of_year

print(day_of_year(2000, 12, 31))