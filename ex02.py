import networkx as nx
import matplotlib.pyplot as plt

# граф з завдання 1
G = nx.Graph()
G.add_nodes_from(['Station A', 'Station B', 'Station C', 'Station D', 'Station E', 'Station F'])
G.add_edges_from([('Station A', 'Station B'), 
                  ('Station B', 'Station C'), 
                  ('Station C', 'Station D'),
                  ('Station D', 'Station E'),
                  ('Station E', 'Station F'),
                  ('Station F', 'Station A'),
                  ('Station A', 'Station C'),
                  ('Station B', 'Station D')])

dfs_path = list(nx.dfs_edges(G, source='Station A'))  # Пошук у глибину
bfs_path = list(nx.bfs_edges(G, source='Station A'))  # Пошук у ширину

# Результати у вигляді послідовності станцій
dfs_sequence = ['Station A'] + [v for u, v in dfs_path]
bfs_sequence = ['Station A'] + [v for u, v in bfs_path]

print(f"Шлях DFS: {' -> '.join(dfs_sequence)}")
print(f"Шлях BFS: {' -> '.join(bfs_sequence)}")

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()