# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# see: https://leetcode.com/problems/generate-parentheses/


class Solution(object):
    def gen(self, result_arr, curr_result, left, right):
        """
        :param result_arr: keeps all generated strings
        :param curr_result: the current string
        :param left: the count of the left opening brackets
        :param right: the count of the left closing brackets
        """
        if left == 0 and right == 0:
            result_arr.append(curr_result)
            return
        # if left > right -> there is unbalance
        if left <= right:
            if left > 0:
                new_result = curr_result + "("
                self.gen(result_arr, new_result, left - 1, right)

            if right > 0:
                new_result = curr_result + ")"
                self.gen(result_arr, new_result, left, right - 1)

    def generateParenthesis(self, n):
        result = []
        self.gen(result_arr=result, curr_result="", left=n, right=n)
        return all


sln = Solution()

print(sln.generateParenthesis(n=3))
print(sln.generateParenthesis(n=4))
