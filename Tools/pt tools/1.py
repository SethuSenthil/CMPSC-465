import networkx as nx
import matplotlib.pyplot as plt

def add_nodes_edges(tree, elements):
    for i in range(len(elements) - 1):
        tree.add_edge(elements[i], elements[i + 1])

# Elements in ascending order
elements = list(range(1, 13))

# Create the graph
tree = nx.DiGraph()
add_nodes_edges(tree, elements)

# Draw the tree
pos = nx.spring_layout(tree)
nx.draw(tree, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Worst-Case Insertion Order Tree \n Sethu Senthil")
plt.show()