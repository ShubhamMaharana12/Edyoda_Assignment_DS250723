# 10) Write a program to find the smallest number using a stack.

# Program:-

class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


stack = MinStack()

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    if user_input == 'q':
        break
    
    try:
        value = int(user_input)
        stack.push(value)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

smallest = stack.get_min()
if smallest is not None:
    print("Smallest number:", smallest)
else:
    print("Stack is empty.")