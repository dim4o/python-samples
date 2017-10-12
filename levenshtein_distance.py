def find_levenshtein_dist(first_str, second_str):
    """
    Finds the minimum distance between two strings
    Dynamic programming implementation. Example:
        k i t t e n
      0 1 2 3 4 5 6
    s 1 1 2 3 4 5 6
    i 2 2 1 2 3 4 5
    t 3 3 2 1 2 3 4
    t 4 4 3 2 1 2 3
    i 5 5 4 3 2 2 3
    n 6 6 5 4 3 3 2
    g 7 7 6 5 4 4 3

    Rule:
    substitution_cost = 0 if a[i-1] == b[j-1] else 1
    m[i][j] = min(m[i-1][j] + 1, m[i][j-1] + 1, m[i-1][j-1] + substitution_cost)

    :param first_str: the first string
    :param second_str: the second string
    :return: the minimum distance
    """
    rows = len(first_str) + 1
    cols = len(second_str) + 1
    matrix = [[0] * cols for _ in range(rows)]

    for row in range(1, rows):
        matrix[row][0] = row
        for col in range(1, cols):
            matrix[0][col] = col
            substitution_cost = 0 if first_str[row - 1] == second_str[col - 1] else 1
            matrix[row][col] = min(matrix[row - 1][col] + 1, matrix[row][col - 1] + 1,
                                   matrix[row - 1][col - 1] + substitution_cost)

    return matrix[rows - 1][cols - 1]


def normalize_dist(first_str, second_str):
    longer_str = max(len(first_str), len(second_str))
    return (longer_str - find_levenshtein_dist(first_str, second_str)) / float(longer_str)


# test
str_1 = "sitting"
str_2 = "kitten"
dist = normalize_dist(str_1, str_2)

print(dist)

