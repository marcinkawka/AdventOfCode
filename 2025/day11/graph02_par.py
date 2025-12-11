import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import all_simple_paths
from multiprocessing import Pool, cpu_count

def filter_paths(paths_chunk):
    return [p for p in paths_chunk if 'fft' in p and 'dac' in p]

def batched(iterable, batch_size):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch

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
with Pool(processes=32) as pool:
    for filtered in pool.imap_unordered(filter_paths, batched(all_paths, 100_000)):
        valid_paths.extend(filtered)

print(f"There are in total {len(valid_paths)} proper paths")