""" Graph1
(A)----(B)---(D)--(E)  (I)---(J)
   \   |    / |\    \  /
    \  |   /  | \    X
     \ |  /   |  \  / \
      (C)    (F) (G)---(H)

"""

graph1 = {
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

graph2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs(graph, start_node):
    """
    :param graph: a graph represented with adjacency list
    :param start_node: a node from which the traversal starts
    :return: a list of all traversed nodes
    """
    queue = [start_node]
    traversed = [start_node]
    used = set(start_node)

    while queue:
        children = graph.get(queue.pop(0))

        for child in children:
            if child not in used:
                queue.append(child)
                traversed.append(child)
                used.add(child)

    return traversed


v1 = bfs(graph=graph1, start_node="A")
v2 = bfs(graph=graph2, start_node="A")

print(v1)
print(v2)
