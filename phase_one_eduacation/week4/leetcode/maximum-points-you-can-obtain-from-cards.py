class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = 0
        for i in range(k):
            window += cardPoints[i]
        
        res = window
        for i in range(1, k + 1):
            window -= cardPoints[k - i]
            window += cardPoints[0 - i]
            res = max(res, window)
        
        return res
