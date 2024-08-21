def has_cycle(graph):
    visited = set()  # Set to keep track of visited vertices

    # Dictionary to keep track of parent vertices during traversal
    parent = {}

    # Define a nested function explore for DFS traversal
    def explore(v, parent_v):
        visited.add(v)  # Mark current vertex as visited
        for neighbor in graph[v]:  #O(deg(v)) # Iterate over neighbors of the current vertex
            if neighbor != parent_v:  # Skip the vertex we came from (back edge)
                if neighbor in visited:  # Check if the neighbor is already visited
                    return True  # If visited, a cycle is detected
                parent[neighbor] = v  # Set the parent of the neighbor
                if explore(neighbor, v):  # Recursively explore the neighbor
                    return True  # If cycle is detected in the recursion, return True
        return False  # If no cycle is detected, return False

    # Iterate over each vertex in the graph
    for vertex in graph: # O(|V|)
        if vertex not in visited:  # If the vertex is not visited yet
            if explore(vertex, None):  # Start DFS traversal from the vertex
                return True  # If cycle is detected during traversal, return True
    return False  # If no cycle is found in the entire graph, return False

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

print(has_cycle(graph))  # Output: False

graph['E'].append('A')
print(has_cycle(graph))  # Output: True
