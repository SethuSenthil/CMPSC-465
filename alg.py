def merge_and_count(arr, l, m, r):
    # Left subarray
    left = arr[l:m + 1]
    # Right subarray
    right = arr[m + 1:r + 1]
    i = j = 0
    k = l
    swaps = 0 #count inversions

    # Merge the left and right subarrays while counting inversions
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            # Count inversions when an element from the right subarray is chosen
            swaps += (m + 1) - (l + i)
        k += 1

    # Copy any remaining elements from the left subarray
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right subarray
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return swaps


def merge_sort_and_count(arr, l, r):
    count = 0
    if l < r:
        m = (l + r) // 2
        # Recursively count inversions in the left subarray
        count += merge_sort_and_count(arr, l, m)
        # Recursively count inversions in the right subarray
        count += merge_sort_and_count(arr, m + 1, r)
        # Merge and count inversions in the current subarray
        count += merge_and_count(arr, l, m, r)

    return count


# Driver code
arr = [1, 20, 6, 4, 5]
# Call the merge_sort_and_count function and print the result
result = merge_sort_and_count(arr, 0, len(arr) - 1)
print(result)
