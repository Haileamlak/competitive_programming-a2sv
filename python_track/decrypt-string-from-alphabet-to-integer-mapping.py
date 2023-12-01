class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                res = chr(96 + int(s[i - 2:i])) + res
                i -= 3
            else:
                res = chr(96 + int(s[i])) + res
                i -= 1
        
        return res