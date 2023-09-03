# Write a Python program to reverse a string.
# Sample String     : "1234abcd"
# Expected Output   : "dcba4321"

# Solution:-

def rev_str(s):
    return s[::-1]

string_example = "1234abcd"
rev_str= rev_str(string_example)
print(rev_str)