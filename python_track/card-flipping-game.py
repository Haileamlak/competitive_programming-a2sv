class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        front_map = {}
        for i in range(len(fronts)):
            if fronts[i] in front_map:
                front_map[fronts[i]].add(i)
            else:
                temp = {i}
                front_map[fronts[i]] = temp
        print(front_map)
        back_map = {}
        for i in range(len(backs)):
            if backs[i] in back_map:
                back_map[backs[i]].add(i)
            else:
                temp = {i}
                back_map[backs[i]] = temp
        
        res = 10001
        for i in range(len(backs)):
            if backs[i] not in front_map:
                res = min(res, backs[i])
            elif len(front_map[backs[i]] & back_map[backs[i]]) == 0: # (i not in front_map[backs[i]])
                res = min(res, backs[i])

        for i in range(len(fronts)):
            if fronts[i] not in back_map:
                res = min(res, fronts[i])
            elif len(back_map[fronts[i]] & front_map[fronts[i]]) == 0: # (i not in back_map[fronts[i]]) 
                res = min(res, fronts[i])
        
        if res == 10001:
            return 0
        return res
        

            
