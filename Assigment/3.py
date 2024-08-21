def deduplicate_sorted(A):
    if not A:
        return A

    write_index = 1  # The position to write the next unique element
    n = len(A)

    for read_index in range(1, n):
        # If the current element is different from the previous one, it's unique
        if A[read_index] != A[read_index - 1]:
            A[write_index] = A[read_index]
            write_index += 1

    # Truncate the array to contain only the unique elements
    while len(A) > write_index:
        A.pop()

    return A