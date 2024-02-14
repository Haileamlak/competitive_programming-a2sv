class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target > 1:
            if target % 2 == 1:
                target -= 1
            elif maxDoubles:
                target //= 2
                maxDoubles -= 1
            else:
                res += target - 2
                target = 1
            
            res += 1
        
        return res