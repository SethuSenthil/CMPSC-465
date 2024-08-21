from collections import deque

def can_obtain_ticket(start, target, modulo):

    # Create a queue to store the nodes to be visited
    queue = deque([start])  # O(1) - Adding an element to the queue
    visited = set()  # O(1) - Creating an empty set
    visited.add(start)  # O(1) - Adding an element to the set

    while queue:
        current = queue.popleft()  # O(1) - Removing the leftmost element from the queue

        # Check if we've reached the target
        if current == target:  # O(1) - Comparing two values

            return True

        # Compute neighbors
        neighbor1 = (current * current) % modulo  # O(1) - Performing arithmetic operations
        neighbor2 = (current * current + 1) % modulo  # O(1) - Performing arithmetic operations

        # Add neighbors to the queue if not visited
        if neighbor1 not in visited:  # O(1) - Checking if an element is in the set
            visited.add(neighbor1)  # O(1) - Adding an element to the set
            queue.append(neighbor1)  # O(1) - Adding an element to the queue

        if neighbor2 not in visited:  # O(1) - Checking if an element is in the set
            visited.add(neighbor2)  # O(1) - Adding an element to the set
            queue.append(neighbor2)  # O(1) - Adding an element to the queue

    return False

# Parameters
start = 1
target = 20
modulo = 400

# Execute
print(can_obtain_ticket(start, target, modulo))  # O(N), where N is the number of elements in the queue