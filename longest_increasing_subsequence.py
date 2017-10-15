def find_longest_increasing_seq(arr):
    """
    Finds the longest increasing subsequence in array of numbers.
           i j
    arr  = 3 4 -1 0 6 2 3
    help = 1 1  1 1 1 1 1

    :param arr:
    :return:
    """
    help = [1] * len(arr)
    re_arr = [-1] * len(arr)
    longest_seq = []
    longest_seq_index = 0
    j = 0
    i = 1
    while i < len(arr):
        while j < i:
            if arr[j] < arr[i]:
                help[i] = max(help[i], help[j] + 1)
                re_arr[i] = j
                if help[i] > help[longest_seq_index]:
                    longest_seq_index = i
            j += 1
        i += 1
        j = 0

    # reconstruct the longest sequence
    while longest_seq_index >= 0:
        longest_seq.append(arr[longest_seq_index])
        longest_seq_index = re_arr[longest_seq_index]

    longest_seq.reverse()

    return longest_seq


# test
seq_len = find_longest_increasing_seq([3, 4, -1, 0, 6, 2, 3, 6, 5])
print seq_len  # [-1, 0, 2, 3, 6]

print find_longest_increasing_seq([3])  # [3]

print find_longest_increasing_seq([3, 1])  # [3]

print find_longest_increasing_seq([3, 4])  # [3, 4]
