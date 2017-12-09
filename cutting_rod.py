def maximize_profit(rods, total_len):
    """
    Given a rod of length and prices at which different length of this rod can sell,
    how do you cut this rod to maximize profit.
    For better context see: https://youtu.be/IRwVmTmN6go

    Example:
    rod = (length, value)
         0  1  2  3  4  5
         0  0  0  0  0  0
    (5)2 0  0  5  5 10 10
    (2)1 0  2  5  7 10 12
    (7)3 0  2  5  7 10 12
    (8)4 0  2  5  7 10 12 -> best_value = 12 = 5 + 5 + 2 = [2, 2, 1]

    Rule:
    if rods[i - 1][0] > j:
        matrix[i][j] = matrix[i - 1][j]
    else:
        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - rods[i - 1][0]] + rods[i - 1][1])

    :param rods: a list of rods
    :param total_len: the given length
    :return: list of lengths - the best way to cut the given length
    """
    rows = len(rods) + 1
    cols = total_len + 1
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if rods[i - 1][0] > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - rods[i - 1][0]] + rods[i - 1][1])

    # reconstruct the result
    path = []
    rows -= 1
    cols -= 1
    while rows > 0 and cols > 0:
        if matrix[rows][cols] == matrix[rows - 1][cols]:
            rows -= 1
        else:
            path.append(rods[rows - 1][0])
            cols -= rods[rows - 1][0]
    print(path)


# test
maximize_profit([(1, 2), (2, 5), (3, 7), (4, 8)], 5)  # [2, 2, 1]
maximize_profit([(2, 5), (1, 2), (3, 7), (4, 8)], 5)  # [1, 2, 2]
maximize_profit([(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)], 8)  # [6, 2]
maximize_profit([(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)], 7)  # [3, 2, 2]
maximize_profit([(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)], 6)  # [6]
maximize_profit([(1, 1), (2, 5), (3, 8), (4, 9), (5, 10), (6, 17), (7, 17), (8, 20)], 5)  # [3, 2]
