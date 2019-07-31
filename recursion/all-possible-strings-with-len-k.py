def all_possible_strings_backtrack(input_str, result, k):
    if len(result) == k:
        print("".join(result))
        return

    for i in range(0, len(input_str)):
        result.append(input_str[i])
        all_possible_strings_backtrack(input_str, result, k)
        result.pop()


def all_possible_strings(input_str, result, k):
    if 0 == k:
        print("".join(result))
        return

    for i in range(0, len(input_str)):
        new_result = result + input_str[i]
        all_possible_strings(input_str, new_result, k - 1)


all_possible_strings_backtrack(input_str="ab", result=[], k=3)
print()
all_possible_strings_backtrack(input_str="ab", result=[], k=4)
print()
all_possible_strings_backtrack(input_str="abc", result=[], k=2)

all_possible_strings(input_str="ab", result="", k=3)
print()
all_possible_strings(input_str="ab", result="", k=4)
print()
all_possible_strings(input_str="abc", result="", k=2)
