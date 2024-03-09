class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        minimum = 0
        maximum = min(citations[-1], len(citations))
        while minimum <= maximum:
            mid = minimum + (maximum - minimum) // 2
            if citations[-mid] >= mid:
                minimum = mid + 1
            else:
                maximum = mid - 1
        
        return maximum