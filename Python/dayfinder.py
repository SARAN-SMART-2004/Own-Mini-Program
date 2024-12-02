def condition_check(year, day, c, rem):
    if 1800 <= year < 1900:
        return operations(day, c, rem, offset=3)
    elif 1900 <= year < 2000:
        return operations(day, c, rem, offset=1)
    elif 2000 <= year < 2100:
        return operations(day, c, rem, offset=0)
    elif 2100 <= year < 2200:
        return operations(day, c, rem, offset=5)
    else:
        print("Please enter a year between 1800 and 2200.")
        return None


def operations(day, c, rem, offset):
    result = (day + c + rem + offset) % 7
    return result


def last_two_digits(year):
    return year % 100


def fifty_percent(value):
    return (value + value // 4) % 7


def month_code(month, leap_year=False):
    codes = {
        1: 6, 2: 2, 3: 2, 4: 5, 5: 0, 6: 3,
        7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4
    }
    leap_codes = {
        1: 5, 2: 1, 3: 2, 4: 5, 5: 0, 6: 3,
        7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4
    }
    return leap_codes[month] if leap_year else codes[month]


def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("The given year is a Leap Year.")
        return True
    else:
        print("The given year is not a Leap Year.")
        return False


def display_error():
    print("Invalid date. Ensure the format is DD/MM/YYYY and the date is valid.")
    print("Days should be <= 31, and months <= 12.")
    print("Examples: 01/01/2022, 29/02/2020 (for leap years).")


def day_of_week(day_code):
    days = {
        0: "SUNDAY", 1: "MONDAY", 2: "TUESDAY", 3: "WEDNESDAY",
        4: "THURSDAY", 5: "FRIDAY", 6: "SATURDAY"
    }
    print(f"The given day is: {days[day_code]}.")


def validate_date(day, month, year):
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False
    if month in {4, 6, 9, 11} and day == 31:
        return False
    if month == 2:
        if is_leap_year(year):
            return day <= 29
        return day <= 28
    return True


print("----------------------------------------------------------------------------------")
print("      // ENTER A DATE TO KNOW THE DAY AND CHECK IF IT IS A LEAP YEAR //")
print("                              // SUPPORTED RANGE: 1800-2200 //")
print("----------------------------------------------------------------------------------")
print("NOTE: Use the format DD/MM/YYYY (e.g., 01/05/2073).")

try:
    day, month, year = map(int, input("Enter the date (DD/MM/YYYY): ").split("/"))
    if validate_date(day, month, year):
        leap_year = is_leap_year(year)
        two_digits = last_two_digits(year)
        rem = fifty_percent(two_digits)
        c = month_code(month, leap_year=leap_year)
        day_code = condition_check(year, day, c, rem)
        if day_code is not None:
            day_of_week(day_code)
    else:
        display_error()
except ValueError:
    display_error()

print("----------------------------------------------------------------------------------")
