graph = (
   # A  B  C  D  E
    (0, 6, 0, 1, 0),  # A
    (6, 0, 5, 2, 2),  # B
    (0, 5, 0, 0, 5),  # C
    (1, 2, 0, 0, 1),  # D
    (0, 2, 5, 1, 0),  # E
)

visited = []
unvisited = []
inf = float('inf')
distances = {}
result = []
start_node = 0

for i in range(0, len(graph)):
    distances[i] = inf
    unvisited.append(i)

distances[start_node] = 0

# print(distances)
# print(unvisited)


curr_node = start_node

while True > 0:

    for next_node in range(0, len(graph[curr_node])):

        curr_edge_value = graph[curr_node][next_node]

        if curr_edge_value > 0 and next_node in unvisited:
            next_node_value = curr_edge_value + distances[curr_node]

            # print("distances", distances)
            # print("curr_node", curr_node)
            # print("next_node", next_node)
            if next_node_value <= distances[next_node]:
                distances[next_node] = next_node_value

    visited.append(curr_node)
    # print(curr_node)
    # print(unvisited)
    unvisited.remove(curr_node)
    result.append((curr_node, distances[curr_node]))
    distances.pop(curr_node)

    if len(unvisited) == 0:
        break

    min_pair = min(distances.items(), key=lambda x: x[1])
    print(distances.items())
    curr_node = min_pair[0]

print("Result", result)
# Result [(0, 0), (3, 1), (4, 2), (1, 3), (2, 7)]

