def is_majority_element(arr, x):
    count = 0  # O(1)
    for a in arr:  # O(n)
        if a == x:  # O(1)
            count += 1  # O(1)
    return count > len(arr) // 2  # O(n)

def majority_element_dc(arr):
    # Base case: If the array has only one element, it is the majority element
    if len(arr) == 1:  # O(1)
        return arr[0]  # O(1)

    # Divide: Split the array into two halves
    mid = len(arr) // 2  # O(1)
    left_half = arr[:mid]  # O(n)
    right_half = arr[mid:]  # O(n)

    # Conquer: Recursively check if x is a majority element in both halves
    left_majority = majority_element_dc(left_half)  # T(n/2)
    right_majority = majority_element_dc(right_half)  # T(n/2)

    # Combine: Check if either left_majority or right_majority is a majority element in the entire array
    if is_majority_element(arr, left_majority):  # O(n)
        return left_majority  # O(1)
    elif is_majority_element(arr, right_majority):  # O(n)
        return right_majority  # O(1)
    else:  # O(1)
        return None  # O(1)

# Example usage:
arr = [1, 2, 2, 2, 3, 4, 2, 2, 2]
print(majority_element_dc(arr))  # Output: 2