# Parent class
class Employee:
    def calculate_salary(self):
        print("Calculating salary for a general employee.")

# Child class
class Manager(Employee):
    def calculate_salary(self):
        print("Calculating salary for a manager with specific benefits and bonus.")


# Creating an Employee instance
employee = Employee()
employee.calculate_salary()  


# Creating Manager instance
manager = Manager()
manager.calculate_salary()
