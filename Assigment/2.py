def deduplicate(A):
    n = len(A)
    seen = [None] * n  # Auxiliary array to track seen elements

    i = 0
    while i < n:
        current_value = get(A, i)

        # Check if the current_value is already in the seen array
        if not in_seen(seen, current_value):
            add_to_seen(seen, current_value)
            i += 1  # Move to the next index
        else:
            delete(A, i)
            n -= 1  # Decrement the size of the array after each deletion

    return A

def in_seen(seen, value):
    for elem in seen:
        if elem == value:
            return True
    return False

def add_to_seen(seen, value):
    for i in range(len(seen)):
        if seen[i] is None:
            seen[i] = value
            break
