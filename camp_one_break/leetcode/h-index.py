class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        def can_be(h):
            i = 0
            while i < len(citations) and citations[i] >= h:
                i += 1
            
            return h <= i
        
        minimum = 0
        maximum = len(citations)
        while minimum <= maximum:
            mid = minimum + (maximum - minimum) // 2
            if can_be(mid):
                minimum = mid + 1
            else:
                maximum = mid - 1
        
        return maximum