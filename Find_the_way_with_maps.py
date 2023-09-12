# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

# Program:-

def fun(number):
    n = number*3
    return n
   
lists = [int(i) for i in input("Enter the numbers:-   ").split(",")]  
triple_no = list(map(fun, lists))          
print("Sample list:-     ", lists)               
print("Triple of list numbers:-      ", triple_no)