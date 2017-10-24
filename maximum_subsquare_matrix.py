def find_max_sub_square_matrix(matrix):
    """
    Given a matrix of 0s and 1s. Find biggest sub-square matrix entirely of 1s in this matrix.
    For better context see: https://youtu.be/_Lf1looyJMU

    Example:
      0 1 2 3 4 5 -> indexes
    0 0 0 0 0 0 0
    1 0 0 0 1 1 1
    2 0 1 0 1 2 2
    3 0 0 1 1 2 3 ->
    4 0 1 0 1 2 3 -> maximum sub square matrix size

    Rule:
    if matrix[i - 1][j - 1] == 1:
        mem[i][j] = min(mem[i][j - 1], mem[i - 1][j - 1], mem[i][j - 1]) + 1

    :param matrix: a matrix of zeroes and ones
    :return: the maximum sub square matrix size
    """
    rows = len(matrix) + 1
    cols = len(matrix[0]) + 1
    max_size = 0

    mem = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i - 1][j - 1] == 1:
                mem[i][j] = min(mem[i][j - 1], mem[i - 1][j - 1], mem[i][j - 1]) + 1
                if mem[i][j] > max_size:
                    max_size = mem[i][j]

    return max_size


# test
print find_max_sub_square_matrix([[0, 0, 0], [0, 0, 0]])  # 0
print find_max_sub_square_matrix([[0, 0, 0], [0, 1, 0]])  # 1
print find_max_sub_square_matrix([[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1]])  # 3
print find_max_sub_square_matrix(
    [[0, 0, 1, 1, 1], [1, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]])  # 3
