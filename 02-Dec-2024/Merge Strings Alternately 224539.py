# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

"""
word1 - made from lowercase english letters
word2 - >>


"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        T(n) = O(n + m)
        S(n) = O(n + m)
        """
        n, m = len(word1), len(word2)

        merged = []
        ptr1, ptr2 = 0, 0
        while ptr1 < n or ptr2 < m:
            if ptr1 < n:
                merged.append(word1[ptr1])
                ptr1 += 1
            
            if ptr2 < m:
                merged.append(word2[ptr2])
                ptr2 += 1
        
        return ''.join(merged)