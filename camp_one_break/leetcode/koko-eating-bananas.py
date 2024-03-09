class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_koko_eat(k):
            hours_used = 0
            for bananas in piles:
                hours_used += ceil(bananas / k)
                if hours_used > h:
                    return False
            
            return True
        
        minimum_k = 1
        maximum_k = max(piles)
        while minimum_k < maximum_k:
            mid = minimum_k + (maximum_k - minimum_k) // 2
            if can_koko_eat(mid):
                maximum_k = mid
            else:
                minimum_k = mid + 1
            
        return minimum_k