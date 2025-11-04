# Task 3: Classify a person into an age group

# --------------------------- METHOD 1: Using if-elif-else ---------------------------
def classify_age(age):
    """Classify using nested if-elif-else conditions"""
    # Check for invalid input
    if age < 0:
        print("Invalid Age Entered.")
    # Check if person is a child
    elif age < 13:
        print("You are a Child.")
    # Check if person is a teenager
    elif age < 20:
        print("You are a Teenager.")
    # Check if person is a young adult
    elif age < 35:
        print("You are a Young Adult.")
    # Check if person is an adult
    elif age < 60:
        print("You are an Adult.")
    # If none of the above, person is a senior citizen
    else:
        print("You are a Senior Citizen.")


# Taking user input
age = int(input("Enter your age: "))

# Call the function to classify based on traditional if-elif-else
print("Using if-elif-else method:")
classify_age(age)


# --------------------------- METHOD 2: Using match-case ---------------------------
def classify_age_match(age):
    """Alternative method using Python's match-case statement (introduced in Python 3.10+)"""
    match age:
        # Each case uses a conditional pattern for matching specific age ranges
        case a if a < 0:
            print("Invalid Age Entered.")
        case a if a < 13:
            print("You are a Child.")
        case a if a < 20:
            print("You are a Teenager.")
        case a if a < 35:
            print("You are a Young Adult.")
        case a if a < 60:
            print("You are an Adult.")
        case _:
            # Underscore (_) acts as a default case, similar to 'else'
            print("You are a Senior Citizen.")

# Call the match-case version
print("\nUsing match-case method:")
classify_age_match(age)
              
#if-elif-else Method:
#Uses simple conditional branching to test multiple ranges.
#Each elif checks a different age boundary.
#It executes only one block depending on the first true condition.
#It’s easy to read and widely compatible with all Python versions.

#match-case Method (Python 3.10+):
#Similar to a switch-case in other programming languages.
#Uses pattern matching for cleaner structure.
#case a if condition: allows us to define logical conditions directly.
#case _: acts like a default case, executed when no other case matches.

#Input & Output:
#The user enters their age.
#The program prints their age group using both methods for comparison.