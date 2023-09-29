# 9) Write a program to reverse a stack.

# Program:-

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_stack(stack):
    aux_stack = Stack()

    while not stack.is_empty():
        item = stack.pop()
        aux_stack.push(item)

    # Assign the reversed stack back to the original stack
    stack.items = aux_stack.items

stack = Stack()

while True:
    try:
        user_input = input("Enter an element to push onto the stack (or 'stop' to end): ")
        if user_input.lower() == 'stop':
            break
        stack.push(int(user_input))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Original Stack:", stack.items)

reverse_stack(stack)

print("Reversed Stack:", stack.items)