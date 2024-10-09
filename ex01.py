import networkx as nx
import matplotlib.pyplot as plt

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

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступінь кожної вершини:")
for station, degree in dict(G.degree()).items():
    print(f"{station}: {degree}")

# Показ графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()