def max_subarray_sum(nums):  # Function to find the maximum sum of a subarray
    max_sum = 0  # Variable to store the maximum sum
    current_sum = 0  # Variable to store the current sum

    for num in nums:  # Iterate through each number in the given list (Time complexity: O(n))
        current_sum += num  # Add the current number to the current sum

        if current_sum > max_sum:  # If the current sum is greater than the maximum sum
            max_sum = current_sum  # Update the maximum sum

        if current_sum < 0:  # If the current sum becomes negative
            current_sum = 0  # Reset the current sum to 0

    return max_sum  # Return the maximum sum

if __name__ == "__main__":
    nums = [5, -7, 5, 6, -1, 2, -10, 2]  # Given list of numbers
    max_sum = max_subarray_sum(nums)  # Call the function to find the maximum sum
    print("Maximum sum of a contiguous sequence:", max_sum)  # Print the maximum sum
    # It prints 12 just as given in the question