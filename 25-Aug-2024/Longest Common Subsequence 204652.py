# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        @cache
        def _longestCommonSubsequence(i, j):
            if i == m or j == n:
                return 0
            
            if text1[i] == text2[j]:
                return 1 + _longestCommonSubsequence(i + 1, j + 1)
            
            return max(_longestCommonSubsequence(i + 1, j), _longestCommonSubsequence(i, j + 1))

        return _longestCommonSubsequence(0, 0)
        