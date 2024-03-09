class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        min_radius = 0
        heaters.sort()

        for house in houses:
            left, right = 0, len(heaters) - 1
            radius = float('inf')
            while left <= right:
                mid = left + (right - left) // 2

                radius = min(radius, abs(house - heaters[mid]))

                if heaters[mid] < house:
                    left = mid + 1
                elif heaters[mid] > house:
                    right = mid - 1
                else:
                    break
            
            min_radius = max(min_radius, radius)
            
        return min_radius