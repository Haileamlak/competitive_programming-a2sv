class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_divided_by(divisor):
            summ = 0
            for num in nums:
                summ += ceil(num / divisor) 
            
            return summ
            
        min_divisor = 1
        max_divisor = max(nums)
        while min_divisor <= max_divisor:
            mid = min_divisor + (max_divisor - min_divisor) // 2
            if sum_divided_by(mid) <= threshold:
                max_divisor = mid - 1
            else:
                min_divisor = mid + 1
        
        return min_divisor