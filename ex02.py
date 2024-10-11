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

def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            path.append(node)
            stack.extend(reversed([neighbor for neighbor in graph.neighbors(node) if neighbor not in visited]))
    
    return path

def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            path.append(node)
            queue.extend([neighbor for neighbor in graph.neighbors(node) if neighbor not in visited])
    
    return path

dfs_sequence = dfs(G, 'Station A')
bfs_sequence = bfs(G, 'Station A')

print(f"Шлях DFS: {' -> '.join(dfs_sequence)}")
print(f"Шлях BFS: {' -> '.join(bfs_sequence)}")

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
plt.title("Транспортна мережа міста")
plt.show()