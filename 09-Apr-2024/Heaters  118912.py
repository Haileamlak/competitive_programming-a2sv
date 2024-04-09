# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        heaters.sort()
        houses.sort()

        heaters.append(float('inf'))
        heaters.append(float('-inf'))

        min_radius = 0
        
        heat_ptr = 0
        for house in houses:
            while heaters[heat_ptr] < house:
                heat_ptr += 1
            
            radius = min(abs(house - heaters[heat_ptr]), abs(house - heaters[heat_ptr - 1]))
            min_radius = max(min_radius, radius)
            
        return min_radius