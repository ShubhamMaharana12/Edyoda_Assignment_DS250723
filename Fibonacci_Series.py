# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

# Program:-

first_num = int(input("Enter the first number:- "))
second_num = int(input("Enter the second number:- "))
print(first_num)
while second_num<50:
    print(second_num)
    first_num,second_num = second_num, first_num+second_num