class Solution:
    def hIndex(self, citations: List[int]) -> int:
        freq = [0] * (len(citations) + 1)
        for citation in citations:
            if citation > len(citations):
                freq[len(citations)] += 1
            else:
                freq[citation] += 1
        
        h = 0
        for i in range(len(citations), -1, -1):
            h += freq[i]
            if h >= i:
                return i
        
        return 0