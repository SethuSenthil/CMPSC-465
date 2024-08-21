def find_fixed_point(arr):
    # Initialize low and high pointers
    low = 0
    high = len(arr) - 1

    # Iterate until low and high pointers meet (Binary Search)
    while low <= high:  # O(log n) - Binary search time complexity
        # Calculate mid index
        mid = (low + high) // 2  # O(1)

        # Check if the element at mid is equal to mid
        if mid == arr[mid]:
            return mid
        # If mid is less than the element at mid, search on the left side
        elif mid < arr[mid]:
            high = mid - 1  # O(1)
        # If mid is greater than the element at mid, search on the right side
        else:
            low = mid + 1  # O(1)

    # Return -1 if no fixed point is found
    return -1  # O(1)