class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ''
        
        s_set = set(s)
        
        for i in range(len(s)):
            if s[i].swapcase() not in s_set:
                
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i + 1:])

                return s2 if len(s2) > len(s1) else s1
        
        return s