# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def intValue(letter):
            return str(ord(letter) - ord('a') + 1)

        s = ''.join([intValue(ch) for ch in s])

        for _ in range(k):
            s = str(sum(list(map(int, list(s)))))
        
        return int(s)