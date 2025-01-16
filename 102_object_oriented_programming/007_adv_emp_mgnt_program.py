### **Problem Title: Advanced Employee Management System**
#
# **Problem:**
#
# Create a class `Employee` to manage employee details in a company, with additional features and more complex requirements:
#
# 1. **Attributes**:
#    - `name`: The name of the employee.
#    - `employee_id`: A unique identifier for the employee.
#    - `position`: The job title of the employee (e.g., "Manager", "Engineer").
#    - `salary`: The salary of the employee.
#    - `department`: The department the employee belongs to (e.g., "HR", "IT", "Sales").
#    - `performance_score`: A score between 0 and 100 representing the employee's performance.
#
# 2. **Methods**:
#    - `update_position(new_position, new_salary)`: Updates the employee's position and salary.
#    - `apply_bonus()`: Applies a bonus to the employee's salary based on their performance:
#      - If `performance_score` >= 90, a 20% bonus is applied.
#      - If `performance_score` >= 75, a 10% bonus is applied.
#      - Otherwise, no bonus is applied.
#    - `transfer_department(new_department)`: Transfers the employee to a new department.
#    - `display_details()`: Displays the employee's details, including their name, ID, position, salary, department, and performance score.
#
# ---
#
# **Example Scenario**:
# 1. Create an employee named "John Doe" with:
#    - `employee_id`: 12345
#    - `position`: "Developer"
#    - `salary`: 50,000
#    - `department`: "IT"
#    - `performance_score`: 85
# 2. Display the employee's details.
# 3. Apply a bonus to the employee's salary based on their performance.
# 4. Update their position to "Senior Developer" with a salary of 70,000.
# 5. Transfer the employee to the "Product Development" department.
# 6. Display the updated details.
#
# ---
#
# This problem introduces additional attributes and logic for calculating bonuses and transferring departments. Try solving it, and I’ll evaluate and grade your work! 😊


## My code:
class Employee:
   def __init__(self, name, employee_id, position, salary, department, performance_score):
      self.name = name
      self.employee_id = employee_id
      self.position = position
      self.salary = salary
      self.department = department
      self.performance_score = performance_score

   def update_position(self, new_position, new_salary):
      self.position = new_position
      self.salary = new_salary
      print(f"The updated employee position is {self.position} & salary is {self.salary}.")

   def apply_bonus(self):
      if 100 >= self.performance_score >= 90:
         total_bonus = (20 / 100) * self.salary
      elif 89 >= self.performance_score >= 75:
         total_bonus = (10 / 100) * self.salary
      else:
         total_bonus = 0
         print(f"No bonus applied for your score of {self.performance_score}")
      print(f"The bonus is {total_bonus}, total salary after bonus {self.salary + total_bonus}.")

   def transfer_department(self, new_department):
      self.department = new_department
      print(f"The updated employee department is {self.department}.")

   def display_details(self):
      print(
         f"\nRecord of: {self.name}, Emp Id: {self.employee_id}, \n{self.position}, {self.salary}, {self.department}, {self.performance_score}")


employee = Employee("John Doe", 12345, "Developer", 50000, "IT", 99)
employee.display_details()
employee.apply_bonus()
employee.update_position("Senior Developer", 70000)
employee.transfer_department("Product Development")
employee.display_details()



## AI Code:
# class Employee:
#    def __init__(self, name, employee_id, position, salary, department, performance_score):
#       self.name = name
#       self.employee_id = employee_id
#       self.position = position
#       self.salary = salary
#       self.department = department
#       self.performance_score = performance_score
#
#    def update_position(self, new_position, new_salary):
#       self.position = new_position
#       self.salary = new_salary
#       print(f"The updated employee position is {self.position} & salary is {self.salary}.")
#
#    def apply_bonus(self):
#       if not (0 <= self.performance_score <= 100):
#          print("Invalid performance score. It must be between 0 and 100.")
#          return 0
#
#       if self.performance_score >= 90:
#          bonus = 0.2 * self.salary
#       elif self.performance_score >= 75:
#          bonus = 0.1 * self.salary
#       else:
#          bonus = 0
#          print(f"No bonus applied for your score of {self.performance_score}.")
#       print(f"Bonus: {bonus:.2f}, Total Salary after Bonus: {self.salary + bonus:.2f}.")
#       return bonus
#
#    def transfer_department(self, new_department):
#       self.department = new_department
#       print(f"The updated employee department is {self.department}.")
#
#    def display_details(self):
#       print(f"\nEmployee Details:")
#       print(f"Name: {self.name}")
#       print(f"ID: {self.employee_id}")
#       print(f"Position: {self.position}")
#       print(f"Salary: {self.salary}")
#       print(f"Department: {self.department}")
#       print(f"Performance Score: {self.performance_score}")
#
#
# # Testing the class
# employee = Employee("John Doe", 12345, "Developer", 50000, "IT", 99)
# employee.display_details()
# employee.apply_bonus()
# employee.update_position("Senior Developer", 70000)
# employee.transfer_department("Product Development")
# employee.display_details()



# Key Changes:
# Encapsulation: Introduced better logic to validate attributes like performance score.
# Enhanced Output: Improved formatting and restricted unnecessary print statements.
# Flexible Bonus Method: Bonus calculation only returns the value, while formatted output provides clarity.