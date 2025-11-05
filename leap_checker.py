

# Section 1: Take input from the user
year = int(input("Enter a year: "))

# Section 2: Check leap year conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
