class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        freq = defaultdict(int)
        
        res = 0
        if nums[0] == goal:
            res = 1

        freq[nums[0]] = 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            if nums[i] == goal:
                res += 1
            
            res += freq[nums[i] - goal]
        
            freq[nums[i]] += 1

        return res
        
