# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20

# Solution:-

def sum_of_numbers(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_of_numbers(nums[1:])

sample_list = [8, 2, 3, 0, 7]
print(sum_of_numbers(sample_list)) 