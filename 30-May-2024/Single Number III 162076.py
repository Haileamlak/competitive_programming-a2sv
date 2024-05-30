# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(lambda x, y: x ^ y, nums)
        diff = xor - (xor & (xor - 1))
        
        num1 = num2 = 0
        for num in nums:
            if num & diff:
                num1 ^= num
            else:
                num2 ^= num
        
        return [num1, num2]