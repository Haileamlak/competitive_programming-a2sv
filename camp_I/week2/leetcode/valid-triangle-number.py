class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        res = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = j + 1
            while j < len(nums) - 1:
                while k < len(nums) and nums[k] < nums[i] + nums[j]:
                    k += 1
                
                res += k - j - 1
                
                j += 1
                if j == k:
                    k += 1
        
        return res