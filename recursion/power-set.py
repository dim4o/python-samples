def print_power_set_iteratively(input_set):
    n = len(input_set)
    num = 1 << n  # 2^n
    mask = 1

    for curr in range(0, num):
        curr_set = []
        for i in range(0, n):
            if mask & curr == 1:
                curr_set.append(input_set[i])
            curr = curr >> 1
        print(curr_set)


def print_power_set_recursively(input_set, decision_index, result):
    # The goal: no more decisions when the index is out of bounds
    if decision_index == len(input_set):
        print(result)
        return

    # Choice 1: select the current index and apply the same rule recursively to the next
    result.append(input_set[decision_index])
    print_power_set_recursively(input_set, decision_index + 1, result)

    # Choice 2: do not select the current index and apply the same rule recursively to the next
    result.pop()
    print_power_set_recursively(input_set, decision_index + 1, result)


test_set = ["A", "B", "C", "D"]

print_power_set_recursively(input_set=test_set, decision_index=0, result=[])

print()

print_power_set_iteratively(input_set=test_set)
