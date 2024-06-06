# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        while left < len(s) and s[left] == '0':
            left += 1
        
        if left == len(s):
            return 0
        
        res = 0
        right = left + 1
        while right < len(s):
            if s[right] == '0':
                res += right - left 
                left += 1
            
            right += 1
        
        return res