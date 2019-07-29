def perm(start_index, character_list, used, result):
    """ Prints all permutation of a given list of characters
    :param start_index: the start index of the permutation
    :param character_list: a list of characters
    :param used: a help list with flags for all used characters
    :param result: stores a permutation
    """
    if start_index == len(character_list):
        print(" ".join(result))
    else:
        for i in range(0, len(character_list)):
            if not used[i]:
                used[i] = True
                result[start_index] = character_list[i]

                perm(start_index + 1, character_list, used, result)

                used[i] = False


def print_all_perm(input_str):
    characters = list(input_str)
    n = len(characters)
    used = [False for _ in range(n)]
    result = [0 for _ in range(n)]
    perm(0, character_list=characters, used=used, result=result)


print_all_perm("1234")
print()
print_all_perm("test")
