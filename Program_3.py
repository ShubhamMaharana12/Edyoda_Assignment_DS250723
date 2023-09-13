# Challenge 3: Implement the Complete Student Class.

# Program:-

class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

student = Student()
student.setName(input("\n Enter student name:- \n"))
student.setRollNumber(input("\n Enter student roll number:- \n"))

print("\n Student Name:", student.getName())
print("\n Student Roll Number:\n", student.getRollNumber())