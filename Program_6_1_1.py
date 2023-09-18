# Create a JSON file (employee.json) containing employee information of minimum 5 employees.
# Each employee information consists of Name, DOB, Height, City, State.
# Write a python program that reads this information from the JSON file and saves the information into a list of objects of Employee class.
# Finally print the list of the Employee objects.

#Program:- 

import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

employee_list = []

for i in range(5):
    print(f"Enter details for Employee {i + 1}:\n")
    name = input("Name: \n")
    dob = input("Date of Birth (DD-MM-YYYY): \n")
    height = float(input("Height (in cm): \n"))
    city = input("City: \n")
    state = input("State: \n")
    
    employee_data = {
        "\n Name": name,
        "\n DOB": dob,
        "\n Height": height,
        "\n City": city,
        "\n State": state
    }
    
    employee_list.append(employee_data)

with open("employee.json", "w") as file:
    json.dump(employee_list, file, indent=4)

print("Employee data saved to 'employee.json'")

with open("employee.json", "r") as file:
    employee_data = json.load(file)

employee_objects = []
for data in employee_data:
    employee = Employee(
        data["\n Name"],
        data["\n DOB"],
        data["\n Height"],
        data["\n City"],
        data["\n State"]
    )
    employee_objects.append(employee)

for employee in employee_objects:
    print(f"Name: {employee.name}\n")
    print(f"DOB: {employee.dob}\n")
    print(f"Height: {employee.height}\n")
    print(f"City: {employee.city}\n")
    print(f"State: {employee.state}\n")
    print()