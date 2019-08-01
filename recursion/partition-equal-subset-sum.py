# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.


class Solution(object):
    def can_partition(self, arr, target_sum, curr_sum, start_index):
        if curr_sum == target_sum:
            return True

        if curr_sum > target_sum:
            return False

        for i in range(start_index, len(arr)):
            new_sum = curr_sum + arr[i]
            found = self.can_partition(arr, target_sum, new_sum, i + 1)
            if found:
                return True

        return False

    def canPartition(self, arr):
        target_sum = sum(arr)
        if target_sum % 2 == 1:
            return False
        return self.can_partition(arr=arr, target_sum=target_sum / 2, curr_sum=0, start_index=0)


input_list = [17, 58, 41, 75, 61, 70, 52, 7, 38, 11, 40, 58, 44, 45, 4, 81, 67, 54, 79, 80, 15, 3, 14, 16, 9, 66, 69,
              41, 72, 37, 28, 3, 33, 90, 56, 12, 72, 49, 35, 22, 49, 27, 49, 82, 41, 77, 100, 82, 18, 95, 24, 51, 37, 2,
              34, 82, 70, 53, 73, 32, 90, 98, 81, 22, 73, 76, 79, 40, 27, 62, 45, 96, 36, 15, 63, 28, 54, 88, 63, 37,
              58, 9, 62, 98, 93, 72, 99, 53, 91, 29, 61, 31, 11, 42, 20, 35, 50, 68, 10, 86]
s = Solution()
print(s.canPartition(input_list))
print(s.canPartition([1, 5, 11, 5]))
