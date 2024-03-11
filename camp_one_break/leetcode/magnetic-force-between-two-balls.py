class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def num_of_balls(force):
            res = 0
            curr = float('-inf')
            for pos in position:
                if curr <= pos - force:
                    res += 1
                    curr = pos
            
            return res

        min_force = 0
        max_force = position[-1] - position[0]

        while min_force <= max_force:
            mid_force = min_force + (max_force - min_force) // 2
            if num_of_balls(mid_force) >= m:
                min_force = mid_force + 1
            else:
                max_force = mid_force - 1
        
        return max_force