class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def hours_taken(speed):
            res = 0
            for i in range(len(dist) - 1):
                res += ceil(dist[i] / speed)
            
            res += dist[-1] / speed
            return res
        
        min_speed, max_speed = 1, pow(10, 9)
        while min_speed <= max_speed:
            mid_speed = min_speed + (max_speed - min_speed) // 2
            if hours_taken(mid_speed) <= hour:
                max_speed = mid_speed - 1
            else:
                min_speed = mid_speed + 1
        
        return min_speed if hours_taken(min_speed) <= hour else -1