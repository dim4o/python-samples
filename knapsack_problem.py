def get_knapsack_optimization(weights, values, max_weight):
    """
    Given a bag which can only take certain weight W. Given list of items with their weights and price.
    How do you fill this bag to maximize value of items in the bag.
    For better context see: https://youtu.be/8LusJS5-AGo

    Example:
    val wt 0 1 2 3 4 5 6 7
           0 0 0 0 0 0 0 0
    (1) 1  0 1 1 1 1 1 1 1
    (4) 3  0 1 1 4 5 5 5 5   => max_value = 9val = 4val + 5val <=> 3wt + 4wt = 7wt
    (5) 4  0 1 1 4 5 6 6 9
    (7) 5  0 1 1 4 5 7 8 9

    Rule:
    if j < weights[i]:
        matrix[i][j] = matrix[i-1][j]
    else:
        matrix[i][j] = max(matrix[i-1][j], values[i] + matrix[i-1][j - weights[i]])

    :param weights: a list with weights
    :param values: a list of the values fot the given weights
    :param max_weight: the maximum allowed weight of the bag
    :return: a solution of weights and the corresponding values as 2 dimensional array
    """
    matrix = [[0] * (max_weight + 1) for _ in range(len(weights) + 1)]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if j < weights[i - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], values[i - 1] + matrix[i - 1][j - weights[i - 1]])

    # reconstruct the solution
    solution = []
    i = len(weights)
    j = max_weight
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i - 1][j]:
            solution.append([weights[i - 1], values[i - 1]])
            j -= weights[i - 1]
        i -= 1

    return solution


def print_solution(solution):
    if solution:
        sln = []
        max_wt = 0
        max_val = 0
        for i in range(len(solution)):
            sln.append("{}({})".format(solution[i][0], solution[i][1]))
            max_wt += solution[i][0]
            max_val += solution[i][1]
        print "{} = {}".format(" + ".join(sln), "{}({})".format(max_wt, max_val))
    else:
        print "No solution."


# test
print_solution(get_knapsack_optimization([1, 3, 4, 5], [1, 4, 5, 7], 7))  # 4(5) + 3(4) = 7(9)
print
print_solution(get_knapsack_optimization([5, 4, 3, 1], [7, 5, 4, 1], 7))  # 3(4) + 4(5) = 7(9)
print
print_solution(get_knapsack_optimization([5, 4, 3, 10], [7, 5, 4, 1], 1))  # No solution.
