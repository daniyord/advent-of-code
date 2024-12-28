import networkx as nx


def get_input(filename):
    file = open(filename, "r")

    graph = nx.Graph()

    for line in file:
        line = line.strip()

        nodes = line.split("-")

        graph.add_edge(nodes[0], nodes[1])

    return graph
