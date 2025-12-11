import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import all_simple_paths

G = nx.DiGraph()
counter=0
with open('input.txt', 'r') as f:
    for line in f:
        node1, nodes = line.strip().split(':')
        G.add_node(node1)
        for node2 in nodes.split(' '):
            G.add_node(node2)
            G.add_edge(node1, node2)

paths1 = list(all_simple_paths(G, source='svr', target='fft'))

print("All simple paths from 'svr' to 'fft':")
with open('paths_svr_to_fft.txt', 'w') as out_f:
    for path in paths1:
        out_f.write(','.join(path) + '\n')
counter += len(paths1)
print(f"There are in total {counter} paths")

paths1 = list(all_simple_paths(G, source='svr', target='dac'))

print("All simple paths from 'svr' to 'dac':")
with open('paths_svr_to_dac.txt', 'w') as out_f:
    for path in paths1:
        out_f.write(','.join(path) + '\n')
counter += len(paths1)

print(f"There are in total {counter} paths")

# nx.draw(G, with_labels=True)
# plt.show()