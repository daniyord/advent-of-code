from shared import get_input
import networkx as nx

graph = get_input("input.txt")

result = 0
for clique in nx.enumerate_all_cliques(graph):
    if len(clique) != 3:
        continue

    if not any(item.startswith('t') for item in clique):
        continue

    result += 1

print(result)
