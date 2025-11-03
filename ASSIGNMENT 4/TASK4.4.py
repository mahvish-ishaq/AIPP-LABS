# ZERO-SHOT 
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example
string = "Artificial Intelligence"
print("(ZERO-SHOT)  Number of vowels:", count_vowels(string))

# ONE-SHOT

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Examples
print("(FEW-SHOT)  Number of vowels in 'Hello':", count_vowels("Hello"))  # Output: 2
print("Number of vowels in 'Python':", count_vowels("Python"))  # Output: 1
print("Number of vowels in 'Artificial Intelligence':", count_vowels("Artificial Intelligence")) # Output: 10

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))
