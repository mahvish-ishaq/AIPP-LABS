def is_leap_year(year):
    # A year is a leap year if:
    # 1. It is divisible by 4 AND
    # 2. Either it is NOT divisible by 100 OR it is divisible by 400
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

# Test the function with some example years
def main():
    # Get input from user
    year = int(input("Enter a year to check if it's a leap year: "))
    
    # Check if it's a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
# Example test cases
if __name__ == "__main__":
    main()