from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)  # O(1) - Initialize an empty defaultdict to store the graph

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))  # O(1) - Add an edge to the graph

    # Use Ford-Fulkerson algorithm to find maximum flow
    def ford_fulkerson(self, source, sink):
        def dfs(s, t, parent):
            visited = [False] * self.V  # O(V) - Initialize a visited array
            stack = [(s, float('inf'))]  # O(1) - Initialize a stack with the source node and infinite flow
            visited[s] = True

            while stack:
                u, flow = stack.pop()  # O(1) - Pop the top element from the stack
                for v, capacity in self.graph[u]:  # O(E) - Iterate through the neighbors of node u
                    if not visited[v] and capacity > 0:  # O(1) - Check if the neighbor is not visited and has capacity
                        min_flow = min(flow, capacity)  # O(1) - Calculate the minimum flow
                        parent[v] = (u, min_flow)  # O(1) - Update the parent of the neighbor
                        if v == t:
                            return min_flow  # O(1) - Return the minimum flow if the sink is reached
                        stack.append((v, min_flow))  # O(1) - Push the neighbor and its flow to the stack
                        visited[v] = True

            return 0  # O(1) - Return 0 if no path is found

        max_flow = 0  # O(1) - Initialize the maximum flow
        parent = [-1] * self.V  # O(V) - Initialize an array to store the parent of each node
        while True:
            path_flow = dfs(source, sink, parent)  # O(V * E) - Find a path from source to sink using DFS
            if path_flow == 0:
                break  # O(1) - Break the loop if no path is found
            max_flow += path_flow  # O(1) - Update the maximum flow

            v = sink
            while v != source:
                u = parent[v][0]  # O(1) - Get the parent of the current node
                self.update_residual(u, v, parent[v][1])  # O(E) - Update the residual capacity of the edges
                v = u

            parent = [-1] * self.V  # O(V) - Reset the parent array

        return max_flow  # O(1) - Return the maximum flow

    # Update residual capacities of the edges and their reverse edges
    def update_residual(self, u, v, flow):
        for i, (vertex, capacity) in enumerate(self.graph[u]):  # O(E) - Iterate through the neighbors of node u
            if vertex == v:  # O(1) - Check if the neighbor is the target node
                self.graph[u][i] = (vertex, capacity - flow)  # O(1) - Update the residual capacity
                break

    # Function to find a critical edge in the flow network
    def find_critical_edge(self, source, sink):
        max_flow = self.ford_fulkerson(source, sink)  # O(V * E) - Find the maximum flow in the network

        for u in range(self.V):  # O(V)
            for v, capacity in self.graph[u]:  # O(E) - Iterate through the neighbors of node u
                original_capacity = capacity  # O(1) - Store the original capacity of the edge
                self.update_residual(u, v, float('inf'))  # O(E) - Temporarily decrease the capacity of the edge
                new_max_flow = self.ford_fulkerson(source, sink)  # O(V * E) - Find the new maximum flow
                if new_max_flow < max_flow:  # O(1) - Check if the new maximum flow is less than the original
                    print(f"Critical Edge: ({u} -> {v}), Capacity: {original_capacity}")  # O(1) - Print the critical edge
                self.update_residual(u, v, original_capacity)  # O(E) - Restore the original capacity

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

source = 0
sink = 5

g.find_critical_edge(source, sink)
