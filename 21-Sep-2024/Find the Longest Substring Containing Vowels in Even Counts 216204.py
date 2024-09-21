# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bitmask = 0
        
        first = {0:-1}
        res = 0
        for i in range(len(s)):
            if s[i] in 'aeiou':
                bitmask ^= (1 << 'aeiou'.index(s[i]))
                if bitmask not in first:
                    first[bitmask] = i

            res = max(res, i - first[bitmask])

        return res