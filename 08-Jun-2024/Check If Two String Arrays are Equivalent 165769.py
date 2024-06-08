# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = k = l = 0
        m, n = len(word1), len(word2)

        while i < m and j < n:
            if word1[i][k] != word2[j][l]:
                return False

            k += 1
            if k == len(word1[i]):
                k = 0
                i += 1
            
            l += 1
            if l == len(word2[j]):
                l = 0
                j += 1

        return (i == m and j == n)            