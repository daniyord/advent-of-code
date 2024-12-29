from shared import get_input
import networkx as nx

graph = get_input("input.txt")

max_clique = None

for clique in nx.find_cliques(graph):
    if max_clique is None or len(max_clique) < len(clique):
        max_clique = clique

print(max_clique)

print(",".join(sorted(max_clique)))
