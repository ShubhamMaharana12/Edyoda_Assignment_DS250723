# 8) Write a program to check if all the brackets are closed in a given code snippet.

# Program:-

def are_brackets_balanced(code):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in code:
        if char in '([{':
           
            stack.append(char)
        elif char in ')]}':
           
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            
            stack.pop()

    return not stack

code_snippet = input("Enter a code snippet: ")

if are_brackets_balanced(code_snippet):
    print("All brackets are properly closed.")
else:
    print("Brackets are not properly closed.")