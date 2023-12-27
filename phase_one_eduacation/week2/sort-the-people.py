class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        high = max(heights)
        names_map = {}
        height_count = [0 for _ in range(high + 1)]

        for i in range(len(names)):
            height_count[heights[i]] += 1
            names_map[heights[i]] = names_map.get(heights[i], []) + [names[i]]
        
        res = []
        for i in range(high, -1, -1):
            while height_count[i] > 0:
                res.append(names_map[i][height_count[i] - 1])
                height_count[i] -= 1

        return res