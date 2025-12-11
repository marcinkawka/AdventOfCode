import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import all_simple_paths

G = nx.DiGraph()
counter=0
valid_paths = []
with open('input.txt', 'r') as f:
    for line in f:
        node1, nodes = line.strip().split(':')
        G.add_node(node1)
        for node2 in nodes.split(' '):
            G.add_node(node2)
            G.add_edge(node1, node2)

all_paths = all_simple_paths(G, source='svr', target='out')

print("All simple paths from 'svr' to 'out':")
for path in all_paths:
    if 'fft' in path and 'dac' in path:
        print("Proper path:", path)
        valid_paths.append(path)
    counter+=1
    if counter % 1000000 == 0:
        print(f".",end='', flush=True)                  
# print(f"There are in total {len(all_paths)} paths")

# proper_paths = [path for path in all_paths if 'fft' in path and 'dac' in path]
# for path in proper_paths:
#     print("Proper path:", path)

print(f"There are in total {len(valid_paths)} proper paths")


# nx.draw(G, with_labels=True)
# plt.show()