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

# (A)--1--(D)--6--(E)
#  |     /  |     /|
#  |    /   |    / |
#  3   3    1   5  2
#  |  /     |  /   |
#  | /      | /    |
# (B)---1--(C)-4--(F)


class Edge:
    def __init__(self, node1, node2, value):
        self.node1 = node1
        self.node2 = node2
        self.value = value


graph1 = [
    Edge("A", "B", 3),
    Edge("A", "D", 1),
    Edge("D", "E", 6),
    Edge("D", "C", 1),
    Edge("D", "B", 3),
    Edge("E", "F", 2),
    Edge("F", "C", 4),
    Edge("C", "E", 5),
    Edge("C", "B", 1),
]


def find_min_span_tree(graph):
    """ Finds minimum spanning thee of undirected graph.
    This is a greedy algorithm. the idea is to sort the edges and
    begin to take from the smallest one, omitting the edges that would make a cycle
    :param graph: a graph represented with edges list
    :return: the edges of the minimum spanning tree
    """
    graph = sorted(graph, key=lambda x: x.value)
    ds = DisjointSet()

    # creates a set from all nodes
    nodes = set()
    for edge in graph:
        nodes.add(edge.node1)
        nodes.add(edge.node2)

    # make set for every node
    for node in nodes:
        ds.make_set(node)

    result = []

    for edge in graph:
        rep1 = ds.find_set(edge.node1)
        rep2 = ds.find_set(edge.node2)
        # if the nodes representatives are different - apply union operation and
        # add the edge to the final result list
        if rep1 != rep2:
            ds.union(edge.node1, edge.node2)
            result.append(edge)

    return result


span_tree = find_min_span_tree(graph1)

# prints the final result
for el in span_tree:
    print("{}-{} -> {}".format(el.node1, el.node2, el.value))
