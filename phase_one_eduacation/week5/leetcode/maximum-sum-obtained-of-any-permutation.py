class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        freq = [0 for _ in range(len(nums) + 1)]
        for request in requests:
            freq[request[0]] += 1
            freq[request[1] + 1] -= 1

        for i in range(1, len(nums)):
            freq[i] += freq[i - 1]
        
        freq.pop()

        freq.sort()
        nums.sort()
        res = 0
        for i in range(len(nums)):
            res += nums[i] * freq[i]
        
        return res % (pow(10, 9) + 7)