import networkx as nx


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
    # All else being the same, prioritize moving < over ^ over v over >. I found this through trial and error.

    #     +---+---+
    #     | ^ | A |
    # +---+---+---+
    # | < | v | > |
    # +---+---+---+

    return {
        "A>": "vA",
        "A<": "v<<A",
        "A^": "<A",
        "Av": "<vA",

        ">A": "^A",
        "><": "<<A",
        ">^": "<^A",
        ">v": "<A",

        "<A": ">>^A",
        "<>": ">>A",
        "<^": ">^A",
        "<v": ">A",

        "^A": ">A",
        "^>": "v>A",
        "^<": "<vA",
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


def get_complexity(num_code, depth):
    # print("num_code:", num_code)
    min_complexity = None

    for code in get_num_commands("A" + num_code):
        temp = get_complexity_inner(code, depth)

        if min_complexity is None or temp < min_complexity:
            min_complexity = temp

    num_part = int(num_code.replace("A", "").lstrip("0"))
    # print(min_complexity, num_part, min_complexity * num_part)
    return min_complexity * num_part


def get_complexity_inner(num_code, depth):
    accumulator = {}

    for item in num_code[:-1].split("A"):
        key = f"{item}A"
        if key not in accumulator:
            accumulator[key] = 0
        accumulator[key] += 1

    for _ in range(0, depth):
        new_accumulator = {}

        for key in accumulator:
            value = accumulator[key]

            # print(key, test_dict[key])
            # print(f"A{key}")
            # print(get_dir_commands(f"A{key}"))

            parts = get_dir_commands(f"A{key}")[:-1].split("A")

            for item in parts:
                key = f"{item}A"
                if key not in new_accumulator:
                    new_accumulator[key] = 0

                new_accumulator[key] += value

            # print(new_test_dict)
        accumulator = new_accumulator

    result = 0
    for key in accumulator:
        result += len(key) * accumulator[key]

    # print(accumulator)

    return result
