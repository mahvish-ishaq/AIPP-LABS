# Student class demonstration
# This class stores and displays student details with user interaction

class Student:
    def __init__(self, name, roll_no, course, marks):
        # Constructor initializes attributes
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        """Calculate grade based on marks"""
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "F"

    def display_details(self):
        """Display all details of the student"""
        print("\n--- STUDENT DETAILS ---")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")


# Taking input from user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
course = input("Enter course name: ")
marks = float(input("Enter marks obtained: "))

# Creating object and displaying details
student1 = Student(name, roll_no, course, marks)
student1.display_details()
