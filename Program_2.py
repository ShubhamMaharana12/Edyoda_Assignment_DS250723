# Challenge 2: Implement a Calculator Class.

# Program:-

class Calculator:
    def __init__(self):
        self.num1 = float(input("Enter the First Number: \n"))
        self.num2 = float(input("Enter the Second Number: \n"))
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num1 == 0:
            return "Cannot divide by zero \n"
        return self.num2 / self.num1

obj = Calculator()
print(obj.add())      
print(obj.subtract()) 
print(obj.multiply()) 
print(obj.divide())   