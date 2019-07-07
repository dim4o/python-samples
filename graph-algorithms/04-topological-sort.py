""" Graph1
(J)---->(I)--->(G)---->(H)
                |        |
                |        |
                V        V
(A)---->(B)--->(D)----->(E)
 |       |     ^  ^
 |       |     |  |
 |       V     |  |
 +----->(C)----+  (F)
"""

graph1 = {
    "A": ("B", "C"),
    "B": ("C", "D"),
    "C": "D",
    "D": "E",
    "E": (),
    "F": "D",
    "G": ("D", "H"),
    "H": "E",
    "I": "G",
    "J": "I"
}

graph2 = {
    "A": "C",
    "B": ("C", "D"),
    "C": "E",
    "D": "F",
    "E": "F",
    "F": "G"
}


def dfs(graph, start_node, visited=None, sorted=None):
    """ Performs DFS traversal over a graph
    :param graph: a graph to be traversed
    :param start_node: the starting traversal point
    :param visited: a set of visited nodes
    :param sorted: a list of sorted nodes in reverse order (stack)
    :return: a list of traversed nodes
    """
    if start_node not in visited:
        children = graph.get(start_node)
        visited.add(start_node)

        if children is not None:
            for child_node in children:
                dfs(graph, child_node, visited, sorted)
        sorted.append(start_node)

    return sorted


def topological_sort(graph):
    """ Performs topological sort of graph
    :param graph: a graph to be sorted
    :return: a list of topologically sorted nodes
    """
    sorted_list = []
    visited_list = set()

    # for each node/vertex apply DFS traversal
    for vertex in graph:
        sorted_list = dfs(graph, vertex, visited=visited_list, sorted=sorted_list)

    return list(reversed(sorted_list))


s1 = topological_sort(graph=graph1)  # ['J', 'I', 'G', 'H', 'F', 'A', 'B', 'C', 'D', 'E']
s2 = topological_sort(graph=graph2)  # ['B', 'D', 'A', 'C', 'E', 'F', 'G']

print(s1)
print(s2)
