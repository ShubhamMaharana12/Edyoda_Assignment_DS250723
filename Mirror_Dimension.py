# Write a Python program that accepts a word from the user and reverse it.
# Sample Test Case
# Input : Edyoda
# Output: adoydE


string = input("Enter the String you want to reverse :")
s = " "
for i in string:
    s = i+s
print(s)

