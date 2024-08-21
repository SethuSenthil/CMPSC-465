import heapq  # Importing heapq module for priority queue implementation

def dijkstra_shortest_path(adj_list, start):
    # Initialize distances to all vertices as infinity
    distances = {vertex: float('inf') for vertex in adj_list}  # O(V)
    # Distance from start to itself is 0
    distances[start] = 0  # O(1)
    # Priority queue to store vertices with their current distance
    pq = [(0, start)]  # O(1)

    while pq:  # While priority queue is not empty
        # Get the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(pq)  # O(log V)

        # If current distance is already greater than the known distance, skip
        if current_distance > distances[current_vertex]:  # O(1)
            continue

        # Iterate through neighbors of the current vertex
        for neighbor, weight in adj_list[current_vertex]:  # O(E)
            # Calculate the distance to the neighbor through the current vertex
            distance = current_distance + weight  # O(1)

            # If the new distance is shorter than the known distance, update it
            if distance < distances[neighbor]:  # O(1)
                distances[neighbor] = distance  # O(1)
                # Push the neighbor and its new distance to the priority queue
                heapq.heappush(pq, (distance, neighbor))  # O(log V)

    return distances

def shortest_paths_with_planes_and_roads(roads, planes, start):
    # Merge roads and planes adjacency lists
    adj_list = {city: [] for city in roads.keys() | planes.keys()}  # O(V)
    for city, neighbors in roads.items():  # O(V)
        adj_list[city].extend(neighbors)  # O(E)
    for city, neighbors in planes.items():  # O(V)
        adj_list[city].extend(neighbors)  # O(E)

    # Compute shortest paths using Dijkstra's algorithm
    shortest_paths = dijkstra_shortest_path(adj_list, start)  # O((V + E) * log V)

    return shortest_paths