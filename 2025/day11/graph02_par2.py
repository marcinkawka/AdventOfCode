import networkx as nx
from networkx.algorithms import all_simple_paths
from multiprocessing import Pool, cpu_count

def match_fft_dac(p):
    return ('fft' in p) and ('dac' in p)

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

print("Got all simple paths from 'svr' to 'out', filtering in parallel...")
count = 0
with Pool(processes=32) as pool:
    for ok in pool.imap_unordered(match_fft_dac, all_paths, chunksize=10_000):
        if ok:
            count += 1
            
print(f"There are in total {count} proper paths")