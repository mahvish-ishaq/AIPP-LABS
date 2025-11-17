#TASK 1 - Refactor Nested Conditionals
def discount(price, category):
    if category == "student":
        return price * 0.9 if price > 1000 else price * 0.95
    else:
        return price * 0.85 if price > 2000 else price

#OTHER OPTION
def student_discount(price):
    return price * (0.9 if price > 1000 else 0.95)

def regular_discount(price):
    return price * (0.85 if price > 2000 else 1)

def discount(price, category):
    rules = {
        "student": student_discount,
        "regular": regular_discount
    }
    return rules.get(category, regular_discount)(price)


# ----- User Input -----
price = float(input("Enter price: "))
category = input("Enter category (student/regular): ").lower()

# ----- Output -----
final_price = discount(price, category)
print("Final discounted price:", final_price)
