import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F'])

G.add_weighted_edges_from([
    ('Station A', 'Station B', 5),
    ('Station B', 'Station C', 3),
    ('Station C', 'Station D', 2),
    ('Station D', 'Station E', 4),
    ('Station E', 'Station F', 1),
    ('Station F', 'Station A', 6),
    ('Station A', 'Station C', 7),
    ('Station B', 'Station D', 8)
])

shortest_paths = dict(nx.all_pairs_dijkstra_path(G))  # пошук найкоротших шляхів між усіма вершинами
shortest_path_lengths = dict(nx.all_pairs_dijkstra_path_length(G))  # довжина шляхів

print("Найкоротші шляхи між усіма вершинами та їхня довжина:")
for source, paths in shortest_paths.items():
    for target in paths:
        print(f"Найкоротший шлях від {source} до {target}: {' -> '.join(paths[target])}, Довжина: {shortest_path_lengths[source][target]}")

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Транспортна мережа міста + ваги маршрутів")
plt.show()