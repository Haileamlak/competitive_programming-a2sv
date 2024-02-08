class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        while l < len(s) and s[l] == '0':
            l += 1
        
        if l == len(s):
            return 0
        
        res = 0
        r = l + 1
        while r < len(s):
            if s[r] == '0':
                res += r - l
                l += 1
            
            r += 1
        
        return res