class UnionFind:
    def __init__(self, n):
        # Initialize the UnionFind data structure with 'n' elements
        self.parent = list(range(n))  # O(n) - Create a list where each element is its own parent
        self.rank = [0] * n  # O(n) - Create a list to store the rank of each element

    def find(self, x):
        # Find the root (representative) of the set that 'x' belongs to
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # O(log n) - Path compression optimization
        return self.parent[x]

    def union(self, x, y):
        # Union operation to merge two sets that contain 'x' and 'y'
        root_x = self.find(x)  # O(log n) - Find the root of 'x'
        root_y = self.find(y)  # O(log n) - Find the root of 'y'
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y  # O(1) - Set the parent of 'x' to 'y'
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x  # O(1) - Set the parent of 'y' to 'x'
            else:
                self.parent[root_y] = root_x  # O(1) - Set the parent of 'y' to 'x'
                self.rank[root_x] += 1  # O(1) - Increase the rank of 'x' by 1

def kruskal_max_spanning_tree(graph):
    # Kruskal's algorithm to find the maximum spanning tree of a graph
    edges = sorted((weight, u, v) for u, neighbors in enumerate(graph) for v, weight in neighbors)
    # Sort the edges of the graph in ascending order of weight
    num_vertices = len(graph)  # O(1) - Get the number of vertices in the graph
    uf = UnionFind(num_vertices)  # O(n) - Create a UnionFind data structure with 'num_vertices'
    max_spanning_tree = []  # O(1) - Create an empty list to store the edges of the maximum spanning tree

    for weight, u, v in reversed(edges):
        # Traverse the edges in reverse order (from highest weight to lowest weight)
        if uf.find(u) != uf.find(v):
            # If the vertices 'u' and 'v' are not in the same set (not connected)
            uf.union(u, v)  # O(log n) - Merge the sets containing 'u' and 'v'
            max_spanning_tree.append((u, v, weight))  # O(1) - Add the edge to the maximum spanning tree

    return max_spanning_tree

# Example usage:
graph = [
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (1, 2), (1, 3)],
    [(2, 0), (2, 1), (2, 3)],
    [(3, 0), (3, 1), (3, 2)]
]

max_spanning_tree = kruskal_max_spanning_tree(graph)  # Find the maximum spanning tree of 'graph'
print("Maximum Spanning Tree:", max_spanning_tree)  # Print the maximum spanning tree
