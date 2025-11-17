#TASK 6 – Complexity Reduction
# DICTIONARY MAPPING APPROACH
def grade(score):
    grade_boundaries = {
        90: "A",
        80: "B",
        70: "C",
        60: "D"
    }

    for boundary, letter in grade_boundaries.items():
        if score >= boundary:
            return letter

    return "F"

# ----- User Input + Output -----
score = int(input("Enter score: "))
print("Grade:", grade(score))

# ELIF APPROACH
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ----- User Input + Output -----
score = int(input("Enter score: "))
print("Grade:", grade(score))
