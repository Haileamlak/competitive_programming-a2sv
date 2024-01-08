class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        longest = 0
        left = 0
        for i in range(len(s)):
            while s[i] in window:
                del window[s[left]]
                left += 1
                
            window[s[i]] = i
            longest = max(longest, i - left + 1)
        
        return longest