"""
This is an intuitive implementation of Dijkstra shortest path algorithm without
minimum binary heap + map. It is not so effective but is easier to understand.
"""


class Graph:
    """ An util data structure that represents a graph """
    def __init__(self, edges, undirected=True):
        self.edges_map = {}
        self.adj_map = {}
        self.vertices_set = set()

        for edge in edges:
            self.edges_map[(edge[0], edge[1])] = edge[2]
            if undirected:
                self.edges_map[(edge[1], edge[0])] = edge[2]

            if edge[0] not in self.adj_map:
                self.adj_map[edge[0]] = []
            self.adj_map[edge[0]].append(edge[1])

            if undirected:
                if edge[1] not in self.adj_map:
                    self.adj_map[edge[1]] = []
                self.adj_map[edge[1]].append(edge[0])

            self.vertices_set.add(edge[0])
            self.vertices_set.add(edge[1])

    def get_weight(self, vertex1, vertex2):
        """ Gets the weight of edge that starts with vertex1 and end with vertex2"""
        return self.edges_map[(vertex1, vertex2)]

    def get_adj_vertices(self, vertex):
        """ Gets a list of all adjacent vertices of a given vertex """
        return self.adj_map.get(vertex)

    def get_all_vertices(self):
        """ Gets a set from all vertices """
        return self.vertices_set


graph_edges_1 = [
    ("A", "B", 6),
    ("A", "D", 1),
    ("B", "D", 2),
    ("B", "C", 5),
    ("B", "E", 2),
    ("C", "E", 5),
    ("D", "E", 1),
]

graph_edges_2 = [
    ("A", "B", 5),
    ("A", "D", 9),
    ("A", "E", 2),
    ("B", "C", 2),
    ("C", "D", 3),
    ("F", "D", 2),
    ("E", "F", 3),
]


def find_shortest_path(edges_list, start_vertex):
    """
    Finds the shortest path from a vertex to all other vertices of graph using Dijkstra algorithm
    :param edges_list: a list of edges represented as tuples: (vertex1, vertex2, weight)
    :param start_vertex: the entry point of the algorithm
    :return: a map with the final result in format { vertex: {'dist': dist, 'prev_vertex': prev} }
    """
    # Preparation - init all data structures
    graph = Graph(edges_list)
    distances = {}  # { vertex: {'dist': dist, 'prev_vertex': prev} }
    visited_set = set()
    unvisited_set = graph.get_all_vertices()
    inf = float("inf")
    result = {}  # { vertex: {'dist': dist, 'prev_vertex': prev} }

    # Populate distances: assigns infinity for all distances and 0 to the start vertex
    vertices = graph.get_all_vertices()
    for adj_vertex in vertices:
        distances[adj_vertex] = {"dist": inf, "prev_vertex": None}
    distances[start_vertex] = {"dist": 0, "prev_vertex": None}

    # While the unvisited set is not empty repeat:
    current_vertex = start_vertex
    while unvisited_set:
        adj_vertices = graph.get_adj_vertices(current_vertex)
        # repeats for all adjacent vertices
        for adj_vertex in adj_vertices:
            # if the adjacent vertex is not visited and the calculated new distance
            # is smaller than the old one - assign the smaller distance to the
            # corresponding distance map value
            if adj_vertex not in visited_set:
                new_weight = distances[current_vertex]["dist"] + graph.get_weight(current_vertex, adj_vertex)
                old_weight = distances[adj_vertex]["dist"]

                if new_weight <= old_weight:
                    distances[adj_vertex]["dist"] = new_weight
                    distances[adj_vertex]["prev_vertex"] = current_vertex

        # marks the current node as visited and removes it from unvisited set
        visited_set.add(current_vertex)
        unvisited_set.remove(current_vertex)
        # removes the current node from distances map and add it to the result map
        result[current_vertex] = distances.pop(current_vertex)

        # if the unvisited set is not empty: assigns the vertex with minimum
        # distance to the current node
        if unvisited_set:
            min_dist_item = min(distances.items(), key=lambda x: x[1]["dist"])
            current_vertex = min_dist_item[0]

    return result


def get_path_to(end, result):
    path = []
    curr = end
    while True:
        path.append(curr)
        curr = result[curr]["prev_vertex"]
        if not curr:
            break
    return list(reversed(path)), result[end]["dist"]


# the shortest path from "A" all other vertices
shortest_path_map = find_shortest_path(edges_list=graph_edges_1, start_vertex="A")

# prints the shortest path and distance form "A" to "C"
shortest_pat = get_path_to("C", shortest_path_map)
print(" -> ".join(shortest_pat[0]) + ", dist: {}".format(shortest_pat[1]))  # A -> D -> E -> C, dist: 7

# the shortest path from "A" all other vertices
shortest_path_map = find_shortest_path(edges_list=graph_edges_2, start_vertex="A")

# prints the shortest path and distance form "A" to "D"
shortest_pat = get_path_to("D", shortest_path_map)
print(" -> ".join(shortest_pat[0]) + ", dist: {}".format(shortest_pat[1]))  # A -> E -> F -> D, dist: 7


# for key, value in g.edges_map.items():
#     print(key, value)
#
# for key, value in g.adj_map.items():
#     print(key, value)
#
# print(g.get_weight("E", "D"))
#
# print(g.get_weight("B", "C"))
# print(g.get_weight("C", "B"))
#
# print(g.get_all_vertices())
#
# s = g.get_all_vertices()
#
# s.remove("B")
# print(s)

# print(g.edges_set.get())
#
# s = set()

# graph = (
#    # A  B  C  D  E
#     (0, 6, 0, 1, 0),  # A
#     (6, 0, 5, 2, 2),  # B
#     (0, 5, 0, 0, 5),  # C
#     (1, 2, 0, 0, 1),  # D
#     (0, 2, 5, 1, 0),  # E
# )
#
# visited = []
# unvisited = []
# inf = float('inf')
# distances = {}
# result = []
# start_node = 0
#
# for i in range(0, len(graph)):
#     distances[i] = inf
#     unvisited.append(i)
#
# distances[start_node] = 0
#
# # print(distances)
# # print(unvisited)
#
#
# curr_node = start_node
#
# while True > 0:
#
#     for next_node in range(0, len(graph[curr_node])):
#
#         curr_edge_value = graph[curr_node][next_node]
#
#         if curr_edge_value > 0 and next_node in unvisited:
#             next_node_value = curr_edge_value + distances[curr_node]
#
#             # print("distances", distances)
#             # print("curr_node", curr_node)
#             # print("next_node", next_node)
#             if next_node_value <= distances[next_node]:
#                 distances[next_node] = next_node_value
#
#     visited.append(curr_node)
#     # print(curr_node)
#     # print(unvisited)
#     unvisited.remove(curr_node)
#     result.append((curr_node, distances[curr_node]))
#     distances.extract_min(curr_node)
#
#     if len(unvisited) == 0:
#         break
#
#     min_pair = min(distances.items(), key=lambda x: x[1])
#     print(distances.items())
#     curr_node = min_pair[0]
#
# print("Result", result)
# # Result [(0, 0), (3, 1), (4, 2), (1, 3), (2, 7)]
