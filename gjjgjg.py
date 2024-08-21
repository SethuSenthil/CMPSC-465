from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        # Time complexity: O(1)
        # Adds an edge between vertices u and v with weight w to the graph
        self.graph[u][v] = w

    # A DFS based function to find all reachable vertices from s
    def DFS(self, s, visited):
        # Time complexity: O(V + E)
        # Performs a Depth-First Search starting from vertex s
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i] and self.graph[s][i] > 0:
                self.DFS(i, visited)

    # Returns true if there is a path from source 's' to sink 't' in
    # residual graph. Also fills parent[] to store the path
    def BFS(self, s, t, parent):
        # Time complexity: O(V + E)
        # Performs a Breadth-First Search starting from vertex s
        visited = [False] * (self.V)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v in self.graph[u]:
                if not visited[v] and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    # Ford-Fulkerson algorithm
    def ford_fulkerson(self, source, sink):
        # Time complexity: O(V * E^2)
        # Implements the Ford-Fulkerson algorithm to find the maximum flow in the graph
        parent = [-1] * (self.V)
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow

            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

    # Find critical edges
    def find_critical_edge(self):
        # Time complexity: O(V * E^3)
        # Finds the critical edges in the graph by iteratively decreasing the capacity of each edge and checking if it reduces the maximum flow
        max_flow_original = self.ford_fulkerson(0, self.V - 1)

        for u in self.graph:
            for v in self.graph[u]:
                # Decrease capacity of the edge
                self.graph[u][v] -= 1
                max_flow_new = self.ford_fulkerson(0, self.V - 1)
                # If decreasing capacity reduces max flow, the edge is critical
                if max_flow_new < max_flow_original:
                    print("Critical Edge:", u, "->", v)
                # Reset the capacity of the edge
                self.graph[u][v] += 1


# Example usage:
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

print("Critical Edges:")
g.find_critical_edge()
