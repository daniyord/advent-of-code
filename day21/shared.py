import networkx as nx
from itertools import combinations


def get_numeric_keypad_graph():
    G = nx.DiGraph()

    G.add_edge('7', '4', command="v")
    G.add_edge('4', '7', command="^")

    G.add_edge('7', '8', command=">")
    G.add_edge('8', '7', command="<")

    G.add_edge('8', '5', command="v")
    G.add_edge('5', '8', command="^")

    G.add_edge('8', '9', command=">")
    G.add_edge('9', '8', command="<")

    G.add_edge('9', '6', command="v")
    G.add_edge('6', '9', command="^")

    G.add_edge('4', '1', command="v")
    G.add_edge('1', '4', command="^")

    G.add_edge('4', '5', command=">")
    G.add_edge('5', '4', command="<")

    G.add_edge('5', '2', command="v")
    G.add_edge('2', '5', command="^")

    G.add_edge('5', '6', command=">")
    G.add_edge('6', '5', command="<")

    G.add_edge('6', '3', command="v")
    G.add_edge('3', '6', command="^")

    G.add_edge('1', '2', command=">")
    G.add_edge('2', '1', command="<")

    G.add_edge('2', '0', command="v")
    G.add_edge('0', '2', command="^")

    G.add_edge('2', '3', command=">")
    G.add_edge('3', '2', command="<")

    G.add_edge('3', 'A', command="v")
    G.add_edge('A', '3', command="^")

    G.add_edge('0', 'A', command=">")
    G.add_edge('A', '0', command="<")

    return G


def get_directional_keypad_matrix():
    return {
        "A>": "vA",
        "A<": "v<<A",
        "A^": "<A",
        "Av": "v<A",

        ">A": "^A",
        "><": "<<A",
        ">^": "^<A",
        ">v": "<A",

        "<A": ">>^A",
        "<>": ">>A",
        "<^": ">^A",
        "<v": ">A",

        "^A": ">A",
        "^>": ">vA",
        "^<": "v<A",
        "^v": "vA",

        "vA": "^>A",
        "v>": ">A",
        "v<": "<A",
        "v^": "^A",
    }


def get_num_commands(code):
    result = [""]

    for i in range(0, len(code) - 1):
        parts = get_parts(code[i], code[i + 1])

        new_result = []
        for item1 in result:
            for item2 in parts:
                new_result.append(item1 + item2)

        result = new_result

    return result


def get_parts(start, end):
    graph = get_numeric_keypad_graph()
    result = []

    short_paths = nx.all_shortest_paths(graph, start, end)

    for short_path in short_paths:
        commands = []

        path_graph = nx.path_graph(short_path)

        for pg in path_graph.edges():
            edge = graph.edges[pg[0], pg[1]]
            commands.append(edge["command"])

        commands.append("A")

        result.append("".join(commands))

    return result


def get_dir_commands(code):
    commands = []

    matrix = get_directional_keypad_matrix()

    for i in range(0, len(code) - 1):
        if code[i] == code[i + 1]:
            commands.append("A")
        else:
            commands.append(matrix[code[i:i + 2]])

    return "".join(commands)


def get_complexity(code):
    min_complexity = None

    code1 = get_num_commands("A" + code)

    for code1 in get_num_commands("A" + code):
        # print(code1)

        code2 = get_dir_commands("A" + code1)

        # print(code2)

        code3 = get_dir_commands("A" + code2)

        # print(code1, code2, code3)

        # print(code, code3, len(code3))

        if min_complexity is None or len(code3) < min_complexity:
            min_complexity = len(code3)

    print(min_complexity, code.replace("A", "").lstrip("0"),
          min_complexity * int(code.replace("A", "").lstrip("0")))
    return min_complexity * int(code.replace("A", "").lstrip("0"))
