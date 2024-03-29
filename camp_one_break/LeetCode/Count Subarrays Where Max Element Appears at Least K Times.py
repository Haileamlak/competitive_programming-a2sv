class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        res = 0
        
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == maxx:
                count += 1
            
            while count >= k:
                res += len(nums) - right

                if nums[left] == maxx:
                    count -= 1

                left += 1
        
        return res
