class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        j = len(nums) - 1
        for i in range(len(nums)):
            while j >= i and nums[i] + nums[j] > target:
                j -= 1
            
            if j >= i:
                res += pow(2, j - i)
            else:
                if nums[i] * 2 <= target:
                    res += 1
        
        return res % (pow(10, 9) + 7)