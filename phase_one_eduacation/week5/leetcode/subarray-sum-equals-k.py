class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = defaultdict(int)

        res = 0
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        
        for i in range(len(nums)):
            if nums[i] == k:
                res += 1

            res += freq[nums[i] - k]
            freq[nums[i]] += 1
        
        return res