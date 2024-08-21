def is_cycle_with_vertex_and_edge(G, v, e):
    # Extract the vertices from the edge
    a, b = e

    # Check if there is a path from b to v
    if not is_reachable(G, b, v):  # Time complexity: O(V + E)
        return False

    # Check if there is a path from v to a
    if not is_reachable(G, v, a):  # Time complexity: O(V + E)
        return False

    # If both paths exist, there is a cycle
    return True

def is_reachable(G, start, target):
    # Set to keep track of visited nodes
    visited = set()

    # Stack to perform depth-first search
    stack = [start]

    while stack:
        # Pop the top node from the stack
        node = stack.pop()

        # If the target node is reached, return True
        if node == target:  # Time complexity: O(1)
            return True

        # If the node has not been visited, mark it as visited
        if node not in visited:  # Time complexity: O(1)
            visited.add(node)

            # Add unvisited neighbors to the stack
            for neighbor in G[node]:  # Time complexity: O(E)
                if neighbor not in visited:  # Time complexity: O(1)
                    stack.append(neighbor)

    # If the target node is not reached, return False
    return False