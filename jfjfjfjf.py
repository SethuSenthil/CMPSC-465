import networkx as nx

def find_reachable_vertex(G):
    # Depth-First Search (DFS) function to traverse the graph
    def dfs(graph, start):
        visited = set()  # Set to keep track of visited vertices  # O(1)
        stack = [start]  # Stack to store vertices to visit  # O(1)
        while stack:
            node = stack.pop()  # Pop the top vertex from the stack  # O(1)
            if node not in visited:  # If the vertex is not visited  # O(1)
                visited.add(node)  # Mark it as visited  # O(1)
                # Add unvisited neighbors of the current vertex to the stack
                stack.extend(set(graph.neighbors(node)) - visited)  # O(deg(node))

        return visited

    # Start DFS from an arbitrary vertex (we can choose any vertex, here we choose the first one)
    start_vertex = list(G.nodes)[0]  # O(1)
    visited_from_start = dfs(G, start_vertex)  # O(V + E)

    # If not all vertices are visited, no such vertex exists
    if len(visited_from_start) != len(G.nodes):  # O(1)
        return None

    # Reverse the graph
    G_reversed = G.reverse()  # O(V + E)

    # Perform DFS on the reversed graph
    visited_from_reversed_start = dfs(G_reversed, start_vertex)  # O(V + E)

    # If all vertices are visited in the reversed graph, start_vertex is our answer
    if len(visited_from_reversed_start) == len(G.nodes):  # O(1)
        return start_vertex

    return None

# Example usage
G = nx.DiGraph()  # O(1)
edges = [('a', 'b'), ('a', 'c'), ('b', 'd'), ('c', 'd'), ('d', 'e')]  # O(1)
G.add_edges_from(edges)  # O(E)

reachable_vertex = find_reachable_vertex(G)  # O(V + E)
if reachable_vertex:
    print(f"The vertex from which all other vertices are reachable is: {reachable_vertex}")  # O(1)
else:
    print("There is no vertex from which all other vertices are reachable.")  # O(1)
