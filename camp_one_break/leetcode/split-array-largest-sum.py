class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def helper(summ):
            count = 0
            curr = 0
            for i in range(len(nums)):
                if curr + nums[i] > summ:
                    count += 1
                    curr = nums[i]
                else:
                    curr += nums[i]
            
            return count + 1 <= k
        
        min_sum, max_sum = max(nums), sum(nums)
        while min_sum <= max_sum:
            mid_sum = min_sum + (max_sum - min_sum ) // 2
            if helper(mid_sum):
                max_sum = mid_sum - 1
            else:
                min_sum = mid_sum + 1
        
        return min_sum