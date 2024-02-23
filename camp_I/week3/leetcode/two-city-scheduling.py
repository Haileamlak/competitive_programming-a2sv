class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[0] - x[1]))

        res = 0
        for i in range(len(costs) // 2):
            res += costs[i][0] + costs[len(costs) - 1 - i][1]
        
        return res