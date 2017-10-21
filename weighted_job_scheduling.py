def find_best_schedule(jobs):
    """
    Given certain jobs with start and end time and amount you make on finishing the job,
    find the maximum value you can make by scheduling jobs in non-overlapping way.
    For better context see: https://youtu.be/cr6Ip0J9izc

    Example:
    (start_time, end_time, value)
    (1,3, 5) (2, 5, 6) (4, 6, 5) (6, 7, 4) (5, 8, 11) (7, 9, 2) -> jobs
          5         6         5         4         11         2  -> values
          5         6        10        14         17        16  -> best_values
    The maximum is 17 = 11 + 6

    Rule:
    if jobs[i] and jobs[j] are not overlapped:
        values[i] = max(values[i], values[j] + jobs[i][2])

    :param jobs: list of jobs
    :return: the maximum value you can take from the jobs
    """
    # sort the jobs by the end time
    jobs = sorted(jobs, key=lambda job: job[1])

    values = [jobs[i][2] for i in range(len(jobs))]
    prev_arr = [-1] * len(jobs)
    best_index = 0

    i = 1
    j = 0
    while i < len(values):
        while j < i:
            # if the jobs are not overlapped
            if jobs[j][1] <= jobs[i][0]:
                values[i] = max(values[i], values[j] + jobs[i][2])
                if values[i] > values[best_index]:
                    best_index = i
                prev_arr[i] = j
            j += 1
        i += 1
        j = 0

    # reconstruct the best path
    best_path = []
    while best_index > -1:
        best_path.append(jobs[best_index][2])
        best_index = prev_arr[best_index]

    return best_path


# test
max_path = find_best_schedule([(2, 5, 6), (4, 6, 5), (6, 7, 4), (7, 9, 2), (1, 3, 5), (5, 8, 11)])
print "{} -> {}".format(sum(i for i in max_path), max_path)  # 17 -> [11, 6]
