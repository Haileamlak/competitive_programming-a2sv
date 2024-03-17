class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        total = sum(nums)
        curr = 0
        res = []

        i = 0
        while curr <= total:
            curr += nums[i]
            total -= nums[i]
            res.append(nums[i])
            i += 1
        
        return res
