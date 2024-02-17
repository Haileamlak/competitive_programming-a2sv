class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]
        
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res