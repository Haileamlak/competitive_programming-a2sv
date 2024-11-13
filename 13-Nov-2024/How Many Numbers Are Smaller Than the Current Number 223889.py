# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = index.get(nums[i], []) + [i]
        
        nums.sort()

        less = [0 for _ in range(len(nums))]
        i = 0
        while i < len(nums):
            idxs = index[nums[i]]
            for j in idxs:
                less[j] = i

            i += len(idxs)
        
        return less