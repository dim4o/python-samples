input_matrix = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]]


def get_available_directions(matrix, i, j):
    row_num = len(matrix)
    col_num = len(matrix[0])
    all_directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    available_directions = []

    for direction in all_directions:
        new_i = direction[0] + i
        new_j = direction[1] + j
        if -1 < new_i < row_num and -1 < new_j < col_num and matrix[new_i][new_j] == 1:
            available_directions.append((new_i, new_j))
    return available_directions


def find_path(matrix, start, end, curr_path, longest_path):
    if start == end:
        if len(curr_path) >= len(longest_path):
            longest_path.append(curr_path.copy())

    possible_directions = get_available_directions(matrix, start[0], start[1])

    for direction in possible_directions:
        matrix[start[0]][start[1]] = -1
        curr_path.append(direction)

        find_path(matrix, direction, end, curr_path, longest_path)

        matrix[start[0]][start[1]] = 1
        curr_path.pop()


def find_longest_paths(matrix, start, end):
    longest_paths = []
    find_path(matrix=matrix, start=start, end=end, curr_path=[start], longest_path=longest_paths)
    long_path = max(longest_paths, key=lambda x: len(x))
    print("Longest path:", long_path)
    print("Path length: ", len(long_path))


find_longest_paths(matrix=input_matrix, start=(0, 0), end=(5, 7))
