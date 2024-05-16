# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_palindrome(string):
            for i in range(len(string) // 2):
                if string[i] != string[-1 - i]:
                    return False

            return True

        @cache
        def _partition(i):
            if i == len(s):
                return []

            res = []
            for j in range(i + 1, len(s)):
                curr = s[i:j]
                if is_palindrome(curr):
                    temp = _partition(j)
                    for part in temp:
                        res.append([curr] + part)
            
            if is_palindrome(s[i:]):
                res.append([s[i:]])
                
            return res
        
        return _partition(0)