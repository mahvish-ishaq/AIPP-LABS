# BIASED VERSION
'''def loan_approval(name, gender, income, credit_score):
    if credit_score > 700 and income > 50000:
        if gender == 'male':  # ⚠️ Biased logic
            return f"Loan approved for Mr. {name}"
        else:
            return f"Loan approved for Ms. {name}"
    else:
        return "Loan not approved"
print(loan_approval("John", "male", 60000, 750))
print(loan_approval("Aisha", "female", 60000, 750))
'''

# UNBIASED VERSION
def loan_approval(name, income, credit_score):
    if credit_score > 700 and income > 50000:
        return f"Loan approved for {name}"
    else:
        return f"Loan not approved for {name}"
print(loan_approval("John", 60000, 700))
print(loan_approval("Aisha", 80000, 850))