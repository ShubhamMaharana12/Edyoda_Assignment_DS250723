# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

# Program:-


from ast import literal_eval
                                                                
lists = list(literal_eval(input("Enter the numbers using the comma or use a string:- ")))
square_no = list(map(lambda x : x**2, lists))     
print("Sample list :-  ", lists)
print("Square of the numbers:-  ", square_no)