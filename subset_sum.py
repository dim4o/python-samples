def find_subset_sum(arr, sum):
    """
    Finds if there exists a subset in given list whose sum is same as given sum.

    Example: Construct sum=11 with this elements [2, 3, 7, 8, 10]
    Solution: 11 = 8 + 3
    For better context see: https://youtu.be/s6FhG--P7z0

    :param arr: list of non negative numbers
    :param sum: sum (total)
    :return: a subset of the given list with the given sum (if there is no solution returns empty list)
    """
    matrix = [[False] * (sum + 1) for _ in range(len(arr) + 1)]
    path = []

    for i in range(len(arr) + 1):
        matrix[i][0] = True

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if arr[i-1] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j - arr[i-1]]

    if matrix[len(arr)][sum]:
        i = len(matrix) - 1
        j = len(matrix[0]) - 1
        while i > 0 and j > 0:
            if matrix[i-1][j] == False:
                path.append(arr[i - 1])
                j -= arr[i-1]
            i -= 1

    return path


def print_subset_sum(arr, sum):
    path = find_subset_sum(arr, sum)
    if path:
        print "{} = {}".format(sum, " + ".join(str(_) for _ in path))
    else:
        print "There is no such subset."


# test
print_subset_sum([2, 3, 7, 8, 10], 11)  # 11 = 8 + 3

print_subset_sum([10, 8, 7, 3, 2], 11)  # 11 = 3 + 8

print_subset_sum([5, 4, 8, 11, 7, 1, 0], 31)  # 31 = 7 + 11 + 8 + 5

print_subset_sum([5, 4, 8, 11, 7, 1, 0], 100)  # There is no such subset.
