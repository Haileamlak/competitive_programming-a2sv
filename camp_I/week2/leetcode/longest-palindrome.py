class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd = False
        for value in count.values():
            if value % 2 == 0:
                res += value
            elif not odd:
                res += value
                odd = True
            else:
                res += value - 1
        
        return res