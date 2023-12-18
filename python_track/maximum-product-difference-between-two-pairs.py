class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # nums.sort()

        min1 = 10**4
        min2 = min1

        max1 = 0
        max2 = max1
        
        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num

            elif num > max2:
                max2 = num

            if num < min1:
                min2 = min1
                min1 = num
            
            elif num < min2:
                min2 = num

        return max1 * max2 - min1 * min2

        # return nums[-1] * nums[-2] - nums[0] * nums[1]