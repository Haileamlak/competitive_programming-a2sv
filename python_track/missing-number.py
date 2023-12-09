class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_from_zero_to_n = n * (n + 1) // 2 
        sum_of_nums = sum(nums)
        num = sum_from_zero_to_n - sum_of_nums

        return num
        
        # nums_set = set([i for i in range(len(nums) + 1)])

        # for num in nums:
        #     nums_set.remove(num)
        
        # return list(nums_set)[0]
