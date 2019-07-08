def find_max_non_adjacent_subsequence_sum(sequence):
    """
    Given an array of positive number, find maximum sum subsequence such that elements
    in this subsequence are not adjacent to each other.
    For better context see: https://youtu.be/UtGtF6nc35g

    Example: [4, 1, 1, 4, 2, 1], max_sum = 4 + 4 + 1 = 9
    Rule:
    temp = incl
    incl = max(incl, excl + sequence[i])
    excl = temp
    ...
    max_subseq = max(incl, excl)

    :param sequence: the given sequence
    :return: max subsequence sum
    """
    incl = 0
    excl = 0

    for i in range(len(sequence)):
        temp = incl
        incl = max(incl, excl + sequence[i])
        excl = temp

    return max(incl, excl)


# test
print(find_max_non_adjacent_subsequence_sum(sequence=[1]))  # 1
print(find_max_non_adjacent_subsequence_sum(sequence=[7, 8]))  # 8
print(find_max_non_adjacent_subsequence_sum(sequence=[4, 1, 1, 4, 2, 1]))  # 9
print(find_max_non_adjacent_subsequence_sum(sequence=[1, 2, 9, 10, 6, 7, 12]))  # 28
