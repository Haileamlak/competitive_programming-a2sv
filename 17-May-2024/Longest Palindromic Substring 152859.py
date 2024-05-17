# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def is_palindrome(left, right):
            if left >= right:
                return True
            
            if s[left] != s[right]:
                return False
            
            return is_palindrome(left + 1, right - 1)
        
        res = ''
        for length in range(len(s), 0, -1):
            for i in range(len(s) - length + 1):
                if is_palindrome(i, i + length - 1):
                    return s[i:i + length]
        
        return res