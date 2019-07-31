def parse_to_integer(index, str_num):
    curr_digit = ord(str_num[index]) - ord('0')
    if index == 0:
        return curr_digit

    return curr_digit + parse_to_integer(index - 1, str_num) * 10


def parse_int(int_str):
    return parse_to_integer(len(int_str) - 1, int_str)


print(parse_int("01234567890"))
