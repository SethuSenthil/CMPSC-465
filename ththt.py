def detect_negative_cycle(graph, source):
    # Step 1: Initialize distances
    distance = {v: float('inf') for v in graph}
    distance[source] = 0

    # Step 2: Relax edges V-1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    # Step 3: Check for negative cycles
    for u in graph:
        for v, weight in graph[u]:
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                return True  # Negative cycle detected

    return False  # No negative cycle detected