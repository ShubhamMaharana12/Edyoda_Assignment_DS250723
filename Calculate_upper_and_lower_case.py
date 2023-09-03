# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# Solution:-

def count_char_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

sample_string = 'The Quick Brown Fox'
upper_count, lower_count = count_char_case(sample_string)
print("No. of Upper Case Characters:", upper_count)
print("No. of Lower Case Characters:", lower_count)