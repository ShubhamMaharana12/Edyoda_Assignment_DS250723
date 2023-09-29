# 6) Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# Program:-

def is_operator(char):

    return char in "+-*/"

def postfix_to_prefix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if not is_operator(char):
            
            stack.append(char)
        else:
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            prefix = char + operand1 + operand2
            stack.append(prefix)

    
    return stack[0]


postfix_expression = input("Enter a postfix expression: ")


prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)
     