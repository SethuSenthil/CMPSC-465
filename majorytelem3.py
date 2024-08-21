def find_majority_element(arr):
    # Base case: if the array has only one element, it is the majority element
    if len(arr) == 1:  # O(1)
        return arr[0]  # O(1)

    # Pair up the elements of the array
    pairs = []  # O(1)
    i = 0  # O(1)
    while i < len(arr) - 1:  # O(n)
        if arr[i] == arr[i+1]:  # O(1)
            pairs.append(arr[i])  # O(1)
            i += 2  # O(1)
        else:
            i += 2  # O(1)

    # If there's an unpaired element, add it to the pairs list
    if i == len(arr) - 1:  # O(1)
        pairs.append(arr[i])  # O(1)

    # Recursive call with the pairs list
    return find_majority_element(pairs)  # T(n/2)


# Example usage:
arr = [1, 2, 2, 2, 3, 4, 2, 2, 2]
print(find_majority_element(arr))  # Output: 2
