from collections import deque

def bfs(graph, source, sink, parent):
    visited = [False] * len(graph)  # O(V), initialize visited list
    queue = deque()  # O(1), create a deque
    queue.append(source)  # O(1), enqueue the source node
    visited[source] = True  # O(1), mark the source node as visited

    while queue:  # O(V + E), iterate until the queue is empty
        u = queue.popleft()  # O(1), dequeue a node from the left end of the queue
        for v, capacity, flow in graph[u]:  # O(E), iterate over the neighbors of node u
            if not visited[v] and capacity > flow:  # O(1), check if the neighbor is not visited and there is capacity in the edge
                queue.append(v)  # O(1), enqueue the neighbor
                visited[v] = True  # O(1), mark the neighbor as visited
                parent[v] = u  # O(1), set the parent of the neighbor
    return visited[sink]  # O(1), return whether the sink node is visited

def max_flow_edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)  # O(V), initialize parent list
    max_flow = 0  # O(1), initialize max flow

    while bfs(graph, source, sink, parent):  # O(V * (V + E)), iterate until there is no augmenting path
        path_flow = float("inf")  # O(1), initialize path flow to infinity
        s = sink  # O(1), set s as the sink node
        while s != source:  # O(V), iterate until s reaches the source node
            path_flow = min(path_flow, graph[parent[s]][s][0] - graph[parent[s]][s][1])  # O(1), calculate the minimum flow in the augmenting path
            s = parent[s]  # O(1), move to the parent node

        max_flow += path_flow  # O(1), update the max flow
        v = sink  # O(1), set v as the sink node
        while v != source:  # O(V), iterate until v reaches the source node
            u = parent[v]  # O(1), get the parent of v
            graph[u][v][1] += path_flow  # O(1), increase the flow in the forward edge
            graph[v][u][1] -= path_flow  # O(1), decrease the flow in the backward edge
            v = parent[v]  # O(1), move to the parent node

    return max_flow  # O(1), return the maximum flow

def find_critical_edges(graph, source, sink):
    max_flow = max_flow_edmonds_karp(graph, source, sink)  # O(V * (V + E)), calculate the maximum flow
    critical_edges = []  # O(1), initialize the list of critical edges

    for u in range(len(graph)):  # O(V), iterate over all nodes in the graph
        for v, (capacity, flow) in enumerate(graph[u]):  # O(E), iterate over the neighbors of node u
            if capacity > 0 and flow > 0:  # O(1), check if it's a residual edge
                original_capacity = capacity  # O(1), store the original capacity
                graph[u][v][0] = 0  # O(1), decrease the capacity temporarily
                new_max_flow = max_flow_edmonds_karp(graph, source, sink)  # O(V * (V + E)), calculate the new maximum flow
                if new_max_flow < max_flow:  # O(1), check if the new maximum flow is less than the previous maximum flow
                    critical_edges.append((u, v))  # O(1), add the edge to the list of critical edges
                graph[u][v][0] = original_capacity  # O(1), restore the original capacity

    return critical_edges  # O(1), return the list of critical edges

# Example usage:
graph = [
    [[0, 0], [10, 0], [5, 0], [15, 0], [0, 0]],  # Example graph adjacency list
    [[0, 0], [0, 0], [4, 0], [0, 0], [9, 0]],
    [[0, 0], [0, 0], [0, 0], [10, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [10, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
]
source = 0
sink = 4
critical_edges = find_critical_edges(graph, source, sink)
