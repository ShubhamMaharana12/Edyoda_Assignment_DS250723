# 2) Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# Program:-

def reverse_array(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        
        arr[start], arr[end] = arr[end], arr[start]

    
        start += 1
        end -= 1


input_str = input("Enter integers separated by spaces: ")
arr = list(map(int, input_str.split()))

reverse_array(arr)

print("Reversed array:", arr)
     