class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        from1 = True
        merged = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            if from1:
                merged += word1[i]
                i += 1
                from1 = False
            else:
                merged += word2[j]
                j += 1
                from1 = True
        
        if i < len(word1):
            merged += word1[i:]
        if j < len(word2):
            merged += word2[j:]
        
        return merged
