def transform_and_conquer(graph):
    # Transforming the edge weights to negatives
    transformed_graph = [[(-weight, u, v) for weight, u, v in neighbors] for neighbors in graph]  # O(V * E), transforms the edge weights to negatives

    # Running minimum spanning tree on transformed graph
    min_spanning_tree = kruskal_max_spanning_tree(transformed_graph)  # O(E * log(V)), finds the minimum spanning tree of the transformed graph

    # Turning the edge weights back to positives in the resulting tree
    max_spanning_tree = [(u, v, -weight) for weight, u, v in min_spanning_tree]  # O(E), turns the edge weights back to positives in the resulting tree

    return max_spanning_tree

# Example usage:
graph = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 2), (1, 3)],
    [(2, 0), (2, 1), (2, 3)],
    [(3, 0), (3, 1), (3, 2)]
]

max_spanning_tree = transform_and_conquer(graph)
print("Maximum Spanning Tree:", max_spanning_tree)
