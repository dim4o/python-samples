def get_min_number_of_coins(coin_denominations, total):
    """
    Given coins of certain denominations and a total, how many minimum coins
    would you need to make this total. Note that the denominations are with unlimited supply.
    For better context see: https://youtu.be/Y0ZqKpToTic

    Example:
       0  1   2   3   4   5   6   7   8   9   10  11
       0  12  12  12  12  12  12  12  12  12  12  12
    1  0  1   2   3   4   5   6   7   8   9   10  11
    5  0  1   2   3   4   1   2   3   4   5   2   3
    6  0  1   2   3   4   1   1   2   3   4   2   2
    8  0  1   2   3   4   1   1   2   1   2   2   2
    Total is 11, Denominations are [5, 6].

    Rule:
    if j < coin_denominations[i - 1]:
        matrix[i][j] = matrix[i - 1][j]
    else:
        matrix[i][j] = min(matrix[i][j - coin_denominations[i - 1]] + 1, matrix[i - 1][j])

    :param coin_denominations: the given denominations
    :param total: the target total
    :return: the minimum coin denominations
    """
    matrix = [[0] * (total + 1) for _ in range(len(coin_denominations) + 1)]
    for j in range(1, total + 1):
        matrix[0][j] = total + 1

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if j < coin_denominations[i - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = min(matrix[i][j - coin_denominations[i - 1]] + 1, matrix[i - 1][j])

    # reconstruct solution
    i = len(coin_denominations)
    j = total
    denominations = set()
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            denominations.add(coin_denominations[i - 1])
            j -= coin_denominations[i - 1]
        else:
            i -= 1

    return denominations


def print_solution(coin_denominations, total):
    path = get_min_number_of_coins(coin_denominations, total)
    if len(path) > 0:
        print "Total is {}, Denominations are {}.".format(total, list(path))
    else:
        print "No solution."


print_solution([1, 5, 6, 8], 11)  # Total is 11, Denominations are [5, 6]

print_solution([8, 6, 5, 1], 11)  # Total is 11, Denominations are [5, 6]

print_solution([1, 1, 1, 1], 11)  # Total is 11, Denominations are [1]

print_solution([1, 5, 10, 21, 25], 63)  # Total is 63, Denominations are [21]

print_solution([2, 2], 11)  # No solution.
