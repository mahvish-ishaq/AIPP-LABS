#NOT INCLUSIVE
def greet(name, gender):
    if gender == 'male':
        return f"Welcome Mr. {name}"
    else:
        return f"Welcome Ms. {name}"
print(greet("John", "male"))  # Welcome Mr. John
print(greet("   Aisha   ", "    female   "))  # Welcome Ms. Aisha

# INCLUSIVE
def greet(name, pronouns=None):
    if pronouns:
        return f"Welcome {name}! (Pronouns: {pronouns})"
    return f"Welcome {name}!"
print(greet("John", "he/him"))  # Welcome John! (Pronouns: he/him)
print(greet("Aisha"))  # Welcome Aisha! 