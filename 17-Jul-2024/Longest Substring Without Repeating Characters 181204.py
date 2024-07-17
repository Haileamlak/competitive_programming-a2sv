# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1

            res = max(res, right - left + 1)
            temp.add(s[right])
        
        return res