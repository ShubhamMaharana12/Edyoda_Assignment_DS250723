# 1) Write a program to find all pairs of an integer array whose sum is equal to a given number.

# Program:-

def find_pairs_with_sum(arr, Target_Sum):
    pairs = []
    arr.sort()  
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == Target_Sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < Target_Sum:
            left += 1
        else:
            right -= 1

    return pairs

def main():
    try:
    
        input_str = input("Enter a list of space-separated integers: ")
        arr = list(map(int, input_str.split()))
        
        target_sum = int(input("Enter the target sum: "))

        result = find_pairs_with_sum(arr, target_sum)

        if result:
            print("Pairs with the sum", target_sum, "are:")
            for pair in result:
                print(pair[0], "+", pair[1], "=", target_sum)
        else:
            print("No pairs with the sum", target_sum, "found in the array.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()