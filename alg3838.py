from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        # Initialize the graph with the given number of vertices
        self.V = vertices
        # Create an empty adjacency list to represent the graph
        self.graph = defaultdict(list)  # O(1) for defaultdict initialization

    def add_edge(self, u, v):
        # Function to add an edge from vertex u to vertex v
        self.graph[u].append(v)  # O(1) for appending to a list

    def dfs(self, u, visited, stack):
        # Depth-first search starting from vertex u
        visited[u] = True
        for v in self.graph[u]:
            # Explore all adjacent vertices of u
            if not visited[v]:
                self.dfs(v, visited, stack)
        # Push the current vertex to the stack after visiting all adjacent vertices
        stack.append(u)  # O(1) for appending to a list

    def transpose(self):
        # Function to get the transpose of the graph
        g = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                # Add the reverse edge to the transpose graph
                g.add_edge(v, u)  # O(1) for adding an edge
        return g

    def fill_order(self, u, visited, stack):
        # Fill the stack with vertices in order of their finishing times in DFS
        visited[u] = True
        for v in self.graph[u]:
            if not visited[v]:
                self.fill_order(v, visited, stack)
        stack.append(u)  # O(1) for appending to a list

    def get_SCCs(self):
        # Function to get the strongly connected components (SCCs) of the graph
        stack = []
        visited = {v: False for v in self.graph}  # O(V) for creating the dictionary
        # Perform DFS and fill the stack with vertices in order of their finishing times
        for u in self.graph:
            if not visited[u]:
                self.dfs(u, visited, stack)

        # Get the transpose of the graph
        gr = self.transpose()  # O(V + E) for creating the transpose

        visited = {v: False for v in self.graph}  # O(V) for creating the dictionary

        SCCs = []
        # Process vertices in order of their finishing times and find SCCs
        while stack:
            u = stack.pop()  # O(1) for popping from a list
            if not visited[u]:
                component = []
                # Fill component with vertices in the same SCC
                gr.fill_order(u, visited, component)
                SCCs.append(component)
        return SCCs

def is_central_server(graph):
    # Check if there is only one SCC in the graph
    SCCs = graph.get_SCCs()  # O(V + E) for finding SCCs
    return len(SCCs) == 1