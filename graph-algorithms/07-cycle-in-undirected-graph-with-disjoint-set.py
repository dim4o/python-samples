# ---------- DISJOINT SET START ----------
class Node:
    def __init__(self, data, rank=0):
        self.data = data
        self.rank = rank
        self.parent = self


class DisjointSet:
    def __init__(self):
        self.map = {}

    def union(self, data1, data2):
        """ Applies union operation of two sets
        :return: whether the two representatives belongs to different sets
        """
        root1 = self.find_set(data1)
        root2 = self.find_set(data2)

        if root1 == root2:
            return False

        elif root1.rank >= root2.rank:
            if root1.rank == root2.rank:
                root1.rank = root1.rank + 1
            root2.parent = root1
        else:
            root1.parent = root2

        return True

    def find_set(self, data):
        """ Finds the root node and applies path compression
        :param data: node data
        :return: the representative of the set to which the data belongs
        """
        node = self.map[data]
        if node == node.parent:
            return node

        node.parent = self.find_set(node.parent.data)

        return node.parent

    def make_set(self, data):
        self.map[data] = Node(data)
# ---------- DISJOINT SET END ----------


"""
Graph1
A-----B-----C
|     |     |
|     |     |
|     |     |
F     E-----D
"""


class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


graph1 = [
    Edge("A", "B"),
    Edge("A", "F"),
    Edge("B", "C"),
    Edge("D", "C"),
    Edge("E", "D"),
    Edge("B", "E")
]

# removed B---E connection
graph2 = {
    Edge("A", "B"),
    Edge("A", "F"),
    Edge("B", "C"),
    Edge("D", "C"),
    Edge("E", "D"),
}

# removed E---D connection
graph3 = [
    Edge("A", "B"),
    Edge("A", "F"),
    Edge("B", "C"),
    Edge("D", "C"),
    Edge("B", "E")
]


def has_cycle(graph):
    """ Finds whether a graph has cycle
    :param graph: list of edges representation of a graph
    :return: whether a graph has cycle
    """
    ds = DisjointSet()

    # creates a set of all graph nodes
    node_set = set()
    for edge in graph:
        node_set.add(edge.node1)
        node_set.add(edge.node2)

    for item in node_set:
        ds.make_set(item)

    for edge in graph:
        same_set = ds.union(edge.node1, edge.node2)
        if same_set:
            return True

    return False


print("Graph1:", has_cycle(graph1))
print("Graph2:", has_cycle(graph2))
print("Graph3:", has_cycle(graph3))
