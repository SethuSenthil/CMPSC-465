def detect_negative_cycle(graph, source):
    # Step 1: Initialize distances
    distance = {v: float('inf') for v in graph}  # O(V)

    distance[source] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(len(graph) - 1):  # O(V)
        for u in graph:  # O(V)
            for v, weight in graph[u]:  # O(E)
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:  # O(1)
                    distance[v] = distance[u] + weight

    # Step 3: Check for negative cycles
    for u in graph:  # O(V)
        for v, weight in graph[u]:  # O(E)
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:  # O(1)
                return True  # Negative cycle detected

    return False  # No negative cycle detected