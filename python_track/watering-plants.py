class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        i = -1
        steps = 0
        can = capacity
        while i < len(plants) - 1:
            if can >= plants[i + 1]:
                steps += 1
                can -= plants[i + 1]
                i += 1
            else:
                can = capacity
                steps += (i + 1) * 2 
        
        return steps
                
