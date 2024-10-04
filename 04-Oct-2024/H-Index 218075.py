# Problem: H-Index - https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        freq = [0] * (n + 1)
        for citation in citations:
            if citation > n:
                freq[n] += 1
            else:
                freq[citation] += 1
        
        h = 0
        for i in range(n, -1, -1):
            h += freq[i]
            if h >= i:
                return i
        
        return 0