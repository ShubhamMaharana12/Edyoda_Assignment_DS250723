# Create a JSON file (employee.json) containing employee information of minimum 5 employees.
# Each employee information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class.
# Finally print the list of the Employee objects.

#Program:-

import json

# Define the Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read data from the JSON file
with open("employee.json", "r") as file:
    employee_data = json.load(file)

# Create a list of Employee objects
employee_list = []
for data in employee_data:
    employee = Employee(
        data["\n Name"],
        data["\n DOB"],
        data["\n Height"],
        data["\n City"],
        data["\n State"]
    )
    employee_list.append(employee)

# Print the list of Employee objects
for employee in employee_list:
    print(f"Name: {employee.name}\n")
    print(f"DOB: {employee.dob}\n")
    print(f"Height: {employee.height}\n")
    print(f"City: {employee.city}\n")
    print(f"State: {employee.state}\n")
    print()