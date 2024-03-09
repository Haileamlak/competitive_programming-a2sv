class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_min, h_max = 0, min(len(citations), citations[-1])

        while h_min <= h_max:
            mid = h_min + (h_max - h_min) // 2
            if citations[-mid] >= mid:
                h_min = mid + 1
            else:
                h_max = mid - 1
        
        return h_max