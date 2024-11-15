# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        for ch1, ch2 in zip(word1, word2):
            arr.append(ch1)
            arr.append(ch2)
        
        if len(word1) > len(word2):
            arr.append(word1[len(word2):])
        
        if len(word2) > len(word1):
            arr.append(word2[len(word1):])

        return ''.join(arr)