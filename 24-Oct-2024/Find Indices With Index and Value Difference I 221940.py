# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        prefix_min = [(nums[0], 0)] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] < prefix_min[i - 1][0]:
                prefix_min[i] = (nums[i], i)
            else:
                prefix_min[i] = prefix_min[i - 1]
        
        prefix_max = [(nums[0], 0)] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > prefix_max[i - 1][0]:
                prefix_max[i] = (nums[i], i)
            else:
                prefix_max[i] = prefix_max[i - 1]

        suffix_min = [(nums[-1], len(nums) - 1)] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < suffix_min[i + 1][0]:
                suffix_min[i] = (nums[i], i)
            else:
                suffix_min[i] = suffix_min[i + 1]
        
        suffix_max = [(nums[-1], len(nums) - 1)] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > suffix_max[i + 1][0]:
                suffix_max[i] = (nums[i], i)
            else:
                suffix_max[i] = suffix_max[i + 1]

        for i in range(len(nums) - indexDifference):
            min_left = prefix_min[i]
            max_left = prefix_max[i]

            min_right = suffix_min[i + indexDifference]
            max_right = suffix_max[i + indexDifference]

            if abs(min_left[0] - max_right[0]) >= valueDifference:
                return [min_left[1], max_right[1]]
            
            if abs(max_left[0] - min_right[0]) >= valueDifference:
                return [max_left[1], min_right[1]]
        
        return [-1, -1]
        