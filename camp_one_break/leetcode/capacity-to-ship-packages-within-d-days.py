class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(maximum_weight):
            curr_weight = 0
            days_left = days
            for weight in weights:
                if curr_weight + weight > maximum_weight:
                    days_left -= 1
                    curr_weight = weight
                else:
                    curr_weight += weight

                if days_left == 0:
                    return False

            return True
        
        minimum = max(weights)
        maximum = sum(weights)
        while minimum < maximum:
            mid = minimum + (maximum - minimum) // 2
            if possible(mid):
                maximum = mid
            else:
                minimum = mid + 1
        
        return minimum