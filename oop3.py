"""
How can we utilize the objects created from the class blueprint 
employee , to get the company's total payroll in class Payroll ? 
"""

""" 
By Modify the Payroll class to accept a list of Employee instances.
Implement a method in Payroll to iterate over this list and calculate the total payroll based 
on the salary attribute of each Employee instance
"""


# Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Payroll class
class Payroll:
    def __init__(self):
        # Initialize Employee objects
        self.employees = []

    def add_employee(self, employee):
        # Add an Employee object to the Payroll's employee list
        self.employees.append(employee)

    def calculate_total_payroll(self):
        # Calculate the total payroll
        return sum(employee.salary for employee in self.employees if employee.salary > 0)

# Create Employee objects
emp1 = Employee("Joseph", 1000)
emp2 = Employee("Habiba", 2000)
emp3 = Employee("Bob", 40000)

# Add employees to the payroll
payroll = Payroll()
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.add_employee(emp3)

# Calculating the total payroll
total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")
