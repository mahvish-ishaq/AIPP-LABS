#TASK 3 - Improve Class Design

class Employee:
    """Represents an employee with a name and salary."""

    def __init__(self, name, salary):
        """Initialize employee with name and salary."""
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        """Increase salary by a given percentage."""
        self.salary += self.salary * (percent / 100)

    def display_info(self):
        """Display formatted employee information."""
        print(f"Employee Name: {self.name}")
        print(f"Current Salary: ₹{self.salary:.2f}")

emp_name = input("Enter employee name: ")
emp_salary = float(input("Enter employee salary: "))

e = Employee(emp_name, emp_salary)

percent = float(input("Enter percentage increase: "))
e.increase_salary(percent)

print("\nUpdated Employee Details:")
e.display_info()

