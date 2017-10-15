def find_min_cost_path(matrix):
    """
    Find minimum cost path to reach bottom right from top left
    provided you can only from down and right.
    Example:
    input matrix:     min sums matrix:
    [1, 3, 5, 8],    [1, 4, 9, 17],
    [4, 2, 1, 7], -> [5, 6, 7, 14]
    [4, 3, 2, 3]     [9, 9, 9, 12]
    Minimum cost path is 12 = [1, 3, 2, 1, 2, 3]
    see: https://youtu.be/lBRtnuxg-gU

    :param matrix: 2 dimensional matrix
    :return: the minimum cost path
    """
    rows = len(matrix)
    cols = len(matrix[0])
    min_sums = [[0] * cols for _ in range(rows)]
    path = []

    # calculates first row and first column values
    prev = 0
    for i in range(cols):
        min_sums[0][i] = matrix[0][i] + prev
        prev = min_sums[0][i]
    prev = 0
    for i in range(rows):
        min_sums[i][0] = matrix[i][0] + prev
        prev = min_sums[i][0]

    for row in range(1, len(min_sums)):
        for col in range(1, len(min_sums[0])):
            min_sums[row][col] = matrix[row][col] + min(min_sums[row][col - 1], min_sums[row - 1][col])

    # calculates the remaining part of the minimum sums
    rows -= 1
    cols -= 1
    path.append(matrix[rows][cols])
    while rows > 0 and cols > 0:
        if min_sums[rows][cols - 1] < min_sums[rows - 1][cols]:
            path.append(matrix[rows][cols - 1])
            cols -= 1
        else:
            path.append(matrix[rows - 1][cols])
            rows -= 1

    path.append(matrix[0][0])
    path.reverse()

    return path


def print_min_cost_path(matrix):
    min_path = find_min_cost_path(matrix)
    path_sum = sum(i for i in min_path)
    print "Minimum cost path is {} = {}".format(path_sum, min_path)


# test
test_matrix = [[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]
print_min_cost_path(test_matrix)  # Minimum cost path is 12 = [1, 3, 2, 1, 2, 3]
