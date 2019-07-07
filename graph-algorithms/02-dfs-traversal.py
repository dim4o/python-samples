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


def dfs(graph, start_node, visited=None, traversed=None):
    """
    :param graph: a graph represented with adjacency list
    :param start_node: a node from which the traversal starts
    :param visited: set that keeps the visited nodes
    :param traversed: keeps the nodes in the order they are traversed
    :return: a list of all traversed nodes
    """
    if traversed is None:
        visited = set()

    if traversed is None:
        traversed = []

    # "contains" operation with O(1) time complexity
    if start_node not in visited:
        children_nodes = graph.get(start_node)

        visited.add(start_node)

        # for each child node apply the current function
        for child_node in children_nodes:
            dfs(graph, child_node, visited, traversed)

        traversed.append(start_node)

    return traversed


v1 = dfs(graph=graph1, start_node="A")
v2 = dfs(graph=graph2, start_node="A")

print(v1)
print(v2)
