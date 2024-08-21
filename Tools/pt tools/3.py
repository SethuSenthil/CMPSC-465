def max_crossing_sum(arr, left, mid, right):
    # Include elements on the left of mid
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, left-1, -1):  # Time complexity: O(n)
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    # Include elements on the right of mid
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, right + 1):  # Time complexity: O(n)
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum

    # Return sum of elements on left and right of mid
    return left_sum + right_sum

def max_subarray_sum(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    # Find middle point
    mid = (left + right) // 2

    # Return maximum of following three possible cases:
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the subarray crosses the midpoint
    return max(max_subarray_sum(arr, left, mid),  # Time complexity: O(log n)
               max_subarray_sum(arr, mid + 1, right),  # Time complexity: O(log n)
               max_crossing_sum(arr, left, mid, right))  # Time complexity: O(n)

# Function to find the maximum subarray sum
def find_maximum_subarray(arr):
    return max_subarray_sum(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    nums = [5, -7, 5, 6, -1, 2, -10, 2]  # Given list of numbers
    max_sum = find_maximum_subarray(nums)  # Call the function to find the maximum sum
    print("Maximum sum of a contiguous sequence:", max_sum)  # Print the maximum sum
    # It prints 12 just as given in the question