class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = [0 for _ in range(len(nums))]
        left_product[0] = nums[0]

        right_product = [0 for _ in range(len(nums))]
        right_product[-1] = nums[-1]
        for i in range(1, len(nums)):
            left_product[i] = left_product[i - 1] * nums[i]
            right_product[-1*(i + 1)] = right_product[-1*i] * nums[-1*(i + 1)]
        
        # nums = [0 for _ in range(len(nums))]
        nums[0] = right_product[1]
        nums[-1] = left_product[-2]
        for i in range(1, len(nums) - 1):
            nums[i] = left_product[i - 1] * right_product[i + 1]

        return nums