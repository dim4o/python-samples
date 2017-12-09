def find_longest_palindromic_sequence(input_str):
    """
    Given a string, find longest palindromic subsequence in this string.
    For better context see: https://youtu.be/_nCsPn7_OgI

    Example:
      a g b d b a
      0 1 2 3 4 5 - indexes
    0 1 1 1 1 3 5 -> max_len = 5 -> a b d b a
    1 0 1 1 1 3 3
    2 0 0 1 1 3 1
    3 0 0 0 1 1 1
    4 0 0 0 0 1 1
    5 0 0 0 0 0 1

    Rule: see the first "while" body

    :param input_str: the input string
    :return: string, the longest palindrome
    """
    rows = len(input_str)
    cols = len(input_str)
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        matrix[i][i] = 1

    for jj in range(1, cols):
        i = 0
        j = jj
        while i < cols and j < cols:
            if input_str[i] == input_str[j]:
                matrix[i][j] = matrix[i + 1][j - 1] + 2
            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1])
            i += 1
            j += 1

    # reconstruct the solution
    path = [0] * cols
    i = 0
    j = cols - 1
    if matrix[i][j] == 1:
        return input_str[0]

    while matrix[i][j] != 0:
        if matrix[i][j] == matrix[i + 1][j]:
            i += 1
        elif matrix[i][j] == matrix[i][j - 1]:
            j -= 1
        else:
            path[i] = input_str[i]
            path[j] = input_str[j]
            i += 1
            j -= 1

    solution = ""
    for i in path:
        if i != 0:
            solution += i

    return solution


# test
print(find_longest_palindromic_sequence("a"))  # a
print(find_longest_palindromic_sequence("abcd"))  # a
print(find_longest_palindromic_sequence("abcdc"))  # cdc
print(find_longest_palindromic_sequence("abaab"))  # baab
print(find_longest_palindromic_sequence("agbdba"))  # abdba
print(find_longest_palindromic_sequence("agbdbaga"))  # agbdbga
print(find_longest_palindromic_sequence("agbddba"))  # abddba
