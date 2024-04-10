# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set(nums)
        for num in nums:
            rev_num = 0
            while num:
                rev_num *= 10
                rev_num += num % 10
                
                num //= 10
            
            distinct.add(rev_num)
        
        return len(distinct)