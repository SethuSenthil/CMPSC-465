def merge_and_count(arr, l, m, r): # TOTAL: O(n log n)
    # Left subarray
    left = arr[l:m + 1]  # O(m - l + 1)
    # Right subarray
    right = arr[m + 1:r + 1]  # O(r - m)

    i = j = 0
    k = l
    swaps = 0

    # Merge the left and right subarrays while counting inversions
    while i < len(left) and j < len(right):  # O(m - l + 1) + O(r - m) iterations in the worst case
        if left[i] <= right[j]:  # O(1)
            arr[k] = left[i]  # O(1)
            i += 1  # O(1)
        else:
            arr[k] = right[j]  # O(1)
            j += 1  # O(1)
            # Count inversions when an element from the right subarray is chosen
            swaps += (m + 1) - (l + i)  # O(1)
        k += 1  # O(1)

    # Copy any remaining elements from the left subarray
    while i < len(left):  # At most O(m - l + 1) iterations
        arr[k] = left[i]  # O(1)
        i += 1  # O(1)
        k += 1  # O(1)

    # Copy any remaining elements from the right subarray
    while j < len(right):  # At most O(r - m) iterations
        arr[k] = right[j]  # O(1)
        j += 1  # O(1)
        k += 1  # O(1)

    return swaps  # O(1)


def merge_sort_and_count(arr, l, r): # TOTAL: O(n log^2 n)
    count = 0  # O(1)
    if l < r:  # O(1)
        m = (l + r) // 2  # O(1)
        # Recursively count inversions in the left subarray
        count += merge_sort_and_count(arr, l, m)  # T(n/2) time complexity (each recursive call halves the array size)
        # Recursively count inversions in the right subarray
        count += merge_sort_and_count(arr, m + 1, r)  # T(n/2) time complexity (each recursive call halves the array size)
        # Merge and count inversions in the current subarray
        count += merge_and_count(arr, l, m, r)  # O(n log n) time complexity (merging step)
    return count  # O(1)

# Time Complexity Analysis:
# - The time complexity of the merge_and_count function is dominated by the merging step, which is O(n log n).
# - The time complexity of the merge_sort_and_count function can be expressed with the recurrence relation T(n) = 2T(n/2) + O(n log n).
# - The overall time complexity of the merge_sort_and_count function is O(n log^2 n).
