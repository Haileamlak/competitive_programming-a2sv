# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        for num in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if 1 << i & num:
                    subset.append(nums[i])

            subsets.append(subset)

        return subsets