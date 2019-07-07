"""
Graph1
A-----B-----C
|     |     |
|     |     |
|     |     |
F     E-----D
"""

graph1 = {
    "A": ("B", "F"),
    "B": ("A", "C", "E"),
    "C": ("B", "D"),
    "D": ("C", "E"),
    "E": ("B", "D"),
    "F": "A"
}

# removed B---E connection
graph2 = {
    "A": ("B", "F"),
    "B": ("A", "C"),
    "C": ("B", "D"),
    "D": ("C", "E"),
    "E": "D",
    "F": "A"
}

# removed E---D connection
graph3 = {
    "A": ("B", "F"),
    "B": ("A", "C", "E"),
    "C": ("B", "D"),
    "D": "C",
    "E": "B",
    "F": "A"
}

# complicated graph with many cycles
graph4 = {
    "A": ("B", "C"),
    "B": ("C", "D", "A"),
    "C": ("A", "B", "D"),
    "D": ("B", "C", "F", "G", "E"),
    "E": ("D", "H"),
    "F": "D",
    "G": ("D", "I", "H"),
    "H": ("E", "G"),
    "I": ("G", "J"),
    "J": "I"
}


def dfs(graph, start_node, parent_node=None, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_node)
    children = graph.get(start_node)

    for child in children:
        # if the current child node is not visited and
        # the current child node is not parent node
        # => a cycle exists
        if child != parent_node and child in visited:
            # add None as a flag to the visited set
            visited.add(None)
        if child not in visited:
            dfs(graph, child, start_node, visited)
    # print(start_node)
    return None in visited


has_cycle1 = dfs(graph=graph1, start_node="A")
has_cycle2 = dfs(graph=graph2, start_node="A")
has_cycle3 = dfs(graph=graph3, start_node="A")
has_cycle4 = dfs(graph=graph4, start_node="A")

print("graph1, has cycle: {}, expected: True".format(has_cycle1))
print("graph2, has cycle: {}, expected: False".format(has_cycle2))
print("graph3, has cycle: {}, expected: False".format(has_cycle3))
print("graph4, has cycle: {}, expected: True".format(has_cycle4))
