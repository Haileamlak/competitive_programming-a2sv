class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def possible(tastiness):
            curr = price[0]
            count = 1
            for i in range(1, len(price)):
                if curr + tastiness <= price[i]:
                    count += 1
                    curr = price[i]
            
            return count >= k
        
        min_tastiness, max_tastiness = 1, price[-1]
        while min_tastiness <= max_tastiness:
            mid_tastiness = min_tastiness + (max_tastiness - min_tastiness) // 2
            if possible(mid_tastiness):
                min_tastiness = mid_tastiness + 1
            else:
                max_tastiness = mid_tastiness - 1
        
        return max_tastiness