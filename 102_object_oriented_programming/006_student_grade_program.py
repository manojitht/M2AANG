# ### **Problem Title: Student Grade Management System**
#
# Create a class `Student` that represents a student and manages their grades. The class should include the following:
#
# 1. **Attributes**:
#    - `name`: The name of the student.
#    - `roll_number`: A unique identifier for the student.
#    - `grades`: A dictionary to store the subject names as keys and their respective grades as values.
#
# 2. **Methods**:
#    - `add_grade(subject, grade)`: Adds or updates the grade for a specific subject.
#    - `calculate_average()`: Calculates and returns the average grade of the student.
#    - `display_details()`: Displays the student's name, roll number, and their grades for all subjects.
#
#
# **Example Scenario**:
# 1. Create a student named "Alice" with roll number 101.
# 2. Add grades for three subjects: Math (85), Science (90), and English (78).
# 3. Display the student's details and their grades.
# 4. Calculate and print the average grade.
# 5. Update the grade for Math to 88 and display the updated details.

## My Code:
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade
            print(f"The grade {grade} is updated for subject {subject}.")
        elif subject not in self.grades:
            self.grades[subject] = grade
            print(f"The new subject {subject} added with grade of {grade}")

    def calculate_average(self):
        total_marks = 0
        subject_count = 0
        for subject in self.grades:
            subject_count += 1
            total_marks += self.grades[subject]
        average = total_marks // subject_count
        print(f"The total average of {self.name} is {average}.")

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Student Roll No: {self.roll_number}")
        print(f"Report Card:")
        for subject in self.grades.keys():
            print(f"{subject}: {self.grades[subject]}")


student = Student("Alice", 101)
student.add_grade("Math", 85)
student.add_grade("Science", 90)
student.add_grade("English", 78)
student.display_details()
student.calculate_average()
student.add_grade("Math", 88)
student.display_details()


## AI Code:
# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#         self.grades = {}
#
#     def add_grade(self, subject, grade):
#         if subject in self.grades:
#             print(f"The grade for '{subject}' is updated to {grade}.")
#         else:
#             print(f"The new subject '{subject}' is added with a grade of {grade}.")
#         self.grades[subject] = grade
#
#     def calculate_average(self):
#         if not self.grades:
#             print(f"No grades available for {self.name}.")
#             return 0
#         total_marks = sum(self.grades.values())
#         average = total_marks / len(self.grades)
#         print(f"The average grade of {self.name} is {average:.2f}.")
#         return average
#
#     def display_details(self):
#         print(f"Student Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print("Report Card:")
#         if self.grades:
#             for subject, grade in self.grades.items():
#                 print(f"  - {subject}: {grade}")
#         else:
#             print("  No grades available.")
#
#
# # Test the class
# student = Student("Alice", 101)
# student.add_grade("Math", 85)
# student.add_grade("Science", 90)
# student.add_grade("English", 78)
# student.display_details()
# student.calculate_average()
# student.add_grade("Math", 88)
# student.display_details()

