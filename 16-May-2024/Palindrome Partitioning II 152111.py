# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        s = s[::-1]

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
        
        memo = [-1] * (len(s))
        def _partition(i):
            if i == len(s):
                return 0
            
            if memo[i] != -1:
                return memo[i]

            if is_palindrome(i, n - 1):
                memo[i] = 0
                return 0
            
            res = n - i
            for j in range(i, n - 1):
                if is_palindrome(i, j):
                    res = min(res, 1 + _partition(j + 1))
            
            memo[i] = res
            return res
        
        return _partition(0)