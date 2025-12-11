import networkx as nx
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

def match_fft_dac(p):
    return ('fft' in p) and ('dac' in p)


for cutoff in range(1, 100):
    all_paths = all_simple_paths(G, source='svr', target='out', cutoff=cutoff)
    
    path_count = 0
    for path in all_paths:
        path_count += 1
        if match_fft_dac(path):
            counter += 1
    counter += path_count
    if path_count>0:
        print(f"with cutoff={cutoff} there are {path_count} paths {counter} total proper paths so far")
