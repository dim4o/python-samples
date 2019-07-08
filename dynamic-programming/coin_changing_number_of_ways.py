def find_number_of_ways_to_get_total(denominations, total):
    """
    Given coins of certain denominations and a total, how many ways these coins
    can be combined to get the total.
    For better context see: https://youtu.be/_fgjrs570YE

    Example:
      0  1  2  3  4  5
    0 1  0  0  0  0  0
    2 1  0  1  0  1  0
    1 1  1  2  2  3  3
    3 1  1  2  3  4  5 => min_num = 5

    Rule:
    if j >= denominations[i-1]:
        matrix[i][j] = matrix[i-1][j] + matrix[i][j - denominations[i-1]
    else:
        matrix[i][j] = matrix[i-1][j]

    :param denominations: the given coin denominations
    :param total: the total sum
    :return: how many ways these coins can be combined to get the total
    """
    rows = len(denominations) + 1
    cols = total + 1
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(0, rows):
        matrix[i][0] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            if j >= denominations[i - 1]:
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - denominations[i - 1]]
            else:
                matrix[i][j] = matrix[i - 1][j]

    return matrix[rows - 1][cols - 1]


# test
print(find_number_of_ways_to_get_total([1], 5))  # 1
print(find_number_of_ways_to_get_total([5], 1))  # 0
print(find_number_of_ways_to_get_total([5], 0))  # 1
print(find_number_of_ways_to_get_total([2, 1, 3], 5))  # 5
print(find_number_of_ways_to_get_total([1, 2, 3], 4))  # 4
print(find_number_of_ways_to_get_total([2, 5, 3, 6], 10))  # 5
print(find_number_of_ways_to_get_total([1, 2, 5, 10], 20))  # 40
print(find_number_of_ways_to_get_total([1, 5, 10, 21, 25], 63))  # 114
