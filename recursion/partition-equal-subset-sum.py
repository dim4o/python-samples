# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.
# see: https://leetcode.com/problems/partition-equal-subset-sum/


class Solution(object):
    def can_partition_1(self, arr, start_index, curr_sum, target_sum, cache_map) -> bool:
        if curr_sum == target_sum:
            return True

        if curr_sum > target_sum or len(arr) == start_index:
            return False

        new_sum = curr_sum + arr[start_index]

        # use a cache if it is available
        cache = str(start_index) + str(new_sum)
        if cache in cache_map:
            return cache_map[cache]

        include_new_sum_decision = self.can_partition_1(arr, start_index + 1, new_sum, target_sum, cache_map)
        do_not_include_new_sum_decision = self.can_partition_1(arr, start_index + 1, curr_sum, target_sum, cache_map)
        found = include_new_sum_decision or do_not_include_new_sum_decision

        # add the current result to the cache
        cache_map[cache] = found
        return found

    def can_partition_2(self, arr, target_sum, curr_sum, start_index, cache_map) -> bool:

        if curr_sum == target_sum:
            return True

        if curr_sum > target_sum:
            return False

        for i in range(start_index, len(arr)):
            new_sum = curr_sum + arr[i]

            # use a cache if it is available
            cache = str(i) + str(curr_sum)
            if cache in cache_map:
                return cache_map[cache]

            found = self.can_partition_2(arr, target_sum, new_sum, i + 1, cache_map)
            if found:
                return True

            # add the current result to the cache
            cache_map[cache] = found

        return False

    def canPartition(self, arr):
        target_sum = sum(arr)
        if target_sum % 2 == 1:
            return False
        return self.can_partition_1(arr=arr, target_sum=target_sum / 2, curr_sum=0, start_index=0, cache_map={})


input_list = [17, 58, 41, 75, 61, 70, 52, 7, 38, 11, 40, 58, 44, 45, 4, 81, 67, 54, 79, 80, 15, 3, 14, 16, 9, 66, 69,
              41, 72, 37, 28, 3, 33, 90, 56, 12, 72, 49, 35, 22, 49, 27, 49, 82, 41, 77, 100, 82, 18, 95, 24, 51, 37, 2,
              34, 82, 70, 53, 73, 32, 90, 98, 81, 22, 73, 76, 79, 40, 27, 62, 45, 96, 36, 15, 63, 28, 54, 88, 63, 37,
              58, 9, 62, 98, 93, 72, 99, 53, 91, 29, 61, 31, 11, 42, 20, 35, 50, 68, 10, 86]
s = Solution()
print(s.canPartition(input_list))
print(s.canPartition([1, 5, 11, 5]))
print(s.canPartition([1, 3, 5]))
print(s.canPartition([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]))
