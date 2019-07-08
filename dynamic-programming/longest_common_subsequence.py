def find_longest_common_subseq(str_1, str_2):
    """
    Finds the longest common subsequence(LCS) between two strings.
    see: https://www.youtube.com/watch?v=NnD96abizww&t=2s

    Example:
    str_1 = a b c d a f
    str_2 = a c b c f
    LCS = a b c f

    Memorization table:
        a b c d a f
      0 0 0 0 0 0 0
    a 0 1 1 1 1 1 1
    c 0 1 1 2 2 2 2
    b 0 1 2 2 2 2 2
    c 0 1 2 3 3 3 3
    f 0 1 2 3 3 3 4

    Rule:
    if a[i] == b[j]:
        m[i][j] = m[i-i][j-1] + 1
    else:
        m[i][j] = max(m[i-1][j], n[i][j-1])

    :param str_1: the first string
    :param str_2: the second string
    :return: the longest subsequence
    """
    rows = len(str_2) + 1
    cols = len(str_1) + 1
    matrix = [[0] * cols for _ in range(rows)]
    longest_seq = []

    for row in range(1, rows):
        for col in range(1, cols):
            if str_1[col - 1] == str_2[row - 1]:
                matrix[row][col] = matrix[row - 1][col - 1] + 1
            else:
                matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1])

    # reconstruct the sequence
    while rows > 0 and cols > 0:
        if matrix[rows - 1][cols - 1] == matrix[rows - 1][cols - 2]:
            cols -= 1
        elif matrix[rows - 1][cols - 1] == matrix[rows - 2][cols - 1]:
            rows -= 1
        else:
            longest_seq.append(str_1[cols - 2])  # same as 'str_1[rows - 2]'
            cols -= 1
            rows -= 1

    longest_seq.reverse()
    print(longest_seq)


def print_matrix(matrix):
    """
    Prettify the default matrix print
    """
    for i in range(len(matrix)):
        print(" ".join(str(_) for _ in matrix[i]))


# test
find_longest_common_subseq("abcdaf", "acbcf")
find_longest_common_subseq("acbcf", "abcdaf")
find_longest_common_subseq("ABCBDAB", "BDCABA")
find_longest_common_subseq("BDCABA", "ABCBDAB")
