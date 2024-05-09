# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        person = [(e, s) for e, s in zip(efficiency, speed)]
        person.sort(key = lambda x : x[0], reverse = True)

        res = 0
        curr_total_speed = 0
        speed_heap = []
        
        for curr_efficiency, curr_speed in person:
            min_efficiency = curr_efficiency
            
            curr_total_speed += curr_speed
            heappush(speed_heap, curr_speed)

            if len(speed_heap) > k:
                curr_total_speed -= heappop(speed_heap)
            
            res = max(res, curr_total_speed * min_efficiency)

        return res % 1_000_000_007