# 7) Write a program to convert prefix expression to infix expression.

# Program:-

def is_operator(char):
    
    return char in "+-*/"

def prefix_to_infix(prefix_expression):
    stack = []

  
    reversed_expression = prefix_expression[::-1]

    for char in reversed_expression:
        if not is_operator(char):
          
            stack.append(char)
        else:
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            infix = f"({operand1}{char}{operand2})"
          
            stack.append(infix)

    return stack[0]

prefix_expression = input("Enter a prefix expression: ")

infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)
     