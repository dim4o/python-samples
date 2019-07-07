"""
Simple graph example

1--e1--2
|    / |
e5 e4  e2
| /    |
3--e3--4
"""

"""
Adjacency matrix

The matrix is symmetrical for undirected graphs (main diagonal)
There is no symmetry for undirected graph

"""
adjacency_matrix_graph = [
   # 1  2  3  4
    [0, 1, 0, 0],  # 1
    [1, 0, 1, 1],  # 2
    [1, 1, 0, 1],  # 3
    [0, 1, 1, 0]   # 4
]

"""
Adjacency list/dictionary
"""
adjacency_dict_graph = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4],
    4:  [2, 3]
}

"""
Incidence matrix
"""
incidence_matrix_graph = [
   # 1  2  3  4  5 -> edges
    [1, 0, 0, 0, 1],  # 1
    [1, 1, 0, 1, 0],  # 2
    [0, 0, 1, 1, 1],  # 3
    [0, 1, 1, 0, 0]   # 4
]

"""
Incidence list/dictionary
"""
incidence_matrix_dict = {
    1: ["e1", "e5"],
    2: ["e1", "e2", "e4"],
    3: ["e3", "e4", "e5"],
    4: ["e2", "e3"]
}