def find_max_height(boxes):
    """
    Given boxes of different dimensions, stack them on top of each other to get maximum height
    such that box on top has strictly less length and width than box under it.
    For better context see: https://youtu.be/9mod_xRB-O0

    This algorithm is actually like "longest increasing subsequence" algorithm

    :param boxes: list of boxes (l, w, h)
    :return: list of boxes with maximum height
    """
    # generates all possible boxes
    all_boxes = []
    for box in boxes:
        #                 length  width   height
        all_boxes.append((box[0], box[1], box[2]))
        all_boxes.append((box[0], box[2], box[1]))
        all_boxes.append((box[2], box[1], box[0]))
    all_boxes = sorted(all_boxes, key=lambda b: b[0] * b[1], reverse=True)

    # uses the longest increasing subsequence algorithm to find the maximum height
    max_arr = []
    indexes = [-1] * len(all_boxes)
    for box in all_boxes:
        max_arr.append(box[2])
    best_index = -1

    i = 1
    j = 0
    while i < len(all_boxes):
        while j < i:
            if is_on_top(all_boxes[j], all_boxes[i]):
                max_arr[i] = max_arr[j] + all_boxes[i][2]
                indexes[i] = j
                if max_arr[i] > indexes[best_index]:
                    best_index = i
            j += 1
        i += 1
        j = 0

    # reconstruct the result
    result = []
    while best_index >= 0:
        result.append(all_boxes[best_index])
        best_index = indexes[best_index]
    result.reverse()

    return max_arr[best_index], result


def is_on_top(box_1, box_2):
    """
    Checks whether a box is on top of another box

    :param box_1: list representation of a box
    :param box_2: list representation of a box
    :return: whether box_2 is on top of box_1
    """
    if (box_2[0] < box_1[0] and box_2[1] < box_1[1]) or (box_2[0] < box_1[1] and box_2[1] < box_1[0]):
        return True
    return False


def print_result(result):
    print("Max height: {},  Boxes: {}".format(result[0], result[1]))


# test
print_result(find_max_height(((1, 2, 4), (3, 2, 5))))  # Max height: 11,  Boxes: [(3, 5, 2), (3, 2, 5), (1, 2, 4)]
print_result(find_max_height(((2, 1, 4), (5, 2, 3))))  # Max height: 11,  Boxes: [(5, 3, 2), (3, 2, 5), (2, 1, 4)]
print_result(find_max_height(((4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32))))
# Max height: 60,  Boxes: [(32, 12, 10), (10, 12, 32), (7, 6, 4), (6, 5, 4), (4, 5, 6), (3, 2, 1), (1, 2, 3)]
print_result(find_max_height(((7, 4, 6), (3, 1, 2), (6, 4, 5), (32, 10, 12))))
# Max height: 60,  Boxes: [(32, 12, 10), (12, 10, 32), (7, 6, 4), (6, 5, 4), (5, 4, 6), (3, 2, 1), (2, 1, 3)]
