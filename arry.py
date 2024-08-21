def is_majority_element(arr, x):
    count = 0  # O(1)
    n = len(arr)  # O(1)

    # Count occurrences of x in the array
    for a in arr:  # O(n)
        if a == x:  # O(1)
            count += 1  # O(1)

    # Check if x is a majority element
    if count > n // 2:  # O(1)
        return True  # O(1)
    else:  # O(1)
        return False  # O(1)

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 2, 2, 2]
x = 2
print(is_majority_element(arr, x))  # Output: True
