class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def num_of_trips(x):
            res = 0
            for t in time:
                res += x // t
            
            return res
        
        min_time, max_time = 1, ceil(totalTrips / len(time)) * max(time)
        while min_time <= max_time:
            mid_time = min_time + (max_time - min_time) // 2
            if num_of_trips(mid_time) >= totalTrips:
                max_time = mid_time - 1
            else:
                min_time = mid_time + 1
        
        return min_time