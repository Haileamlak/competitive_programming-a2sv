class Solution:
    def isPathCrossing(self, path: str) -> bool:
        point = [0, 0]

        visited = {(point[0], point[1])}

        for i in range(len(path)):
            if path[i] == "N":
                point[1] += 1
            elif path[i] == "S":
                point[1] -= 1
            elif path[i] == "W":
                point[0] -= 1
            else:
                point[0] += 1

            if (point[0], point[1]) in visited:
                return True
            
            visited.add((point[0], point[1]))
        
        return False