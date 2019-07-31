def is_palindrome(string, i, j):
    sub_str = string[i:j+1]
    rev_str = sub_str[::-1]

    return sub_str == rev_str


def gen_all_pal_dec(in_str, start, result):
    if start == len(in_str):
        print(result)

    for i in range(start, len(in_str)):
        if is_palindrome(in_str, start, i):
            result.append(in_str[start:i + 1])
            gen_all_pal_dec(in_str, i + 1, result)
            result.pop()


def gen_all_palindromic_decompositions(input_str):
    gen_all_pal_dec(in_str=input_str, start=0, result=[])


gen_all_palindromic_decompositions(input_str="nitin")
print()
gen_all_palindromic_decompositions(input_str="geeks")
print()
gen_all_palindromic_decompositions(input_str="aaabbb")
