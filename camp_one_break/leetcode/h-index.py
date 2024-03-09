class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)

        h = 1
        while h <= len(citations) and citations[h - 1] >= h:
            h += 1
        
        return h - 1