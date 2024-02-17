class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            res = 0
            left = 0
            curr = 0
            for right in range(len(nums)):
                curr += nums[right] % 2
                
                while curr > k:
                    curr -= nums[left] % 2
                    left += 1
                
                res += right - left + 1
            
            return res
        
        return at_most(k) - at_most(k - 1)