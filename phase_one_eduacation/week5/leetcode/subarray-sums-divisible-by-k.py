class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        
        freq = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                res += 1
            
            res += freq[nums[i] % k]
            freq[nums[i] % k] += 1
        
        return res