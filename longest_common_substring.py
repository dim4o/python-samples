def find_longest_common_substring(str_1, str_2):
    """
    Given two strings, find longest common substring between them.
    For better context see: https://youtu.be/BysNXJHzCEs

    Example:
      a b c d a f
      0 0 0 0 0 0
    z 0 0 0 0 0 0
    b 0 1 0 0 0 0
    c 0 0 2 0 0 0
    d 0 0 0 3 0 0
    f 0 0 0 0 0 1
    max_len = 3, longest_substring = "dcb"

    Rule:
    if str_1[j - 1] == str_2[i - 1]:
        matrix[i][j] = matrix[i - 1][j - 1] + 1
    else:
        matrix[i][j] = 0

    :param str_1: the first string
    :param str_2: the second string
    :return: the longest common substring
    """
    matrix = [[0] * (len(str_1) + 1) for _ in range(len(str_2) + 1)]
    max_len = 0
    best_row = 0
    best_col = 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if str_1[j - 1] == str_2[i - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_len:
                    max_len = matrix[i][j]
                    best_row = i
                    best_col = j
            else:
                matrix[i][j] = 0

    # reconstruct the solution
    longest_substring = ""
    while matrix[best_row][best_col] > 0:
        longest_substring = str_1[best_col - 1] + longest_substring
        best_row -= 1
        best_col -= 1

    return longest_substring


def print_longest_common_substring(str_1, str_2):
    longest_substring = find_longest_common_substring(str_1, str_2)
    if len(longest_substring) > 0:
        print "Longest common substring between '{}' and '{}': '{}'.".format(str_1, str_2, longest_substring)
    else:
        print "No solution."


# test
print_longest_common_substring("abcdaf", "zbcdf")
# Longest common substring between 'abcdaf' and 'zbcdf': 'bcd'.

print_longest_common_substring("abcdaf", "daf")
# Longest common substring between 'abcdaf' and 'daf': 'daf'.

print_longest_common_substring("ab", "abcdaf")
# Longest common substring between 'ab' and 'abcdaf': 'ab'.

print_longest_common_substring("a", "abcdaf")
# Longest common substring between 'a' and 'abcdaf': 'a'.

print_longest_common_substring("abcdaf", "xyz")
# No solution.

print_longest_common_substring("qwrtertxyztdryhh",
                               "sfdsdtxyzfdsfs")
# vLongest common substring between 'qwrtertxyztdryhh' and 'sfdsdtxyzfdsfs': 'txyz'.
