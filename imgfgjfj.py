import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
edges = [('s', 'a', -2), ('s', 'b', 1), ('a', 'b', 1)]
G.add_weighted_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_color='black', arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=12)

plt.title('Graph for Question 3')
plt.show()