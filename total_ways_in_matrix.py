def calc_total_ways(rows, cols):
    """
    Given a 2 dimensional matrix, how many ways you can reach bottom right
    from top left provided you can only move down and right.
    For better context see: https://youtu.be/GO5QHC_BmvM

    Example with 4x4 matrix:
    1 1 1  1
    1 2 3  4
    1 3 6  10
    1 4 10 20 -> the total number of ways is 20

    :param rows: number of matrix rows
    :param cols: number of matrix columns
    :return: the total number of ways from top left to bottom right corner
    """
    matrix = [[1]*cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[rows - 1][cols - 1]


# test
print calc_total_ways(4, 4)  # 20

print calc_total_ways(4, 1)  # 1

print calc_total_ways(4, 5)  # 35
