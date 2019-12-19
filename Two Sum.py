# Link: https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list, target) -> list:
        num_to_index = {}

        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i
        return []
