class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def num_of_children(num):
            res = 0
            for candie in candies:
                res += candie // num
            
            return res

        minimum = 1
        maximum = max(candies)
        while minimum <= maximum:
            mid = minimum + (maximum - minimum) // 2
            if num_of_children(mid) >= k:
                minimum = mid + 1
            else:
                maximum = mid - 1
        
        return maximum