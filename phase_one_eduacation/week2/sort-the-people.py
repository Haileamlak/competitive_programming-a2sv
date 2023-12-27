class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        high = max(heights)
        names_map = {}
        height_count = [0 for _ in range(high + 1)]

        for i in range(len(names)):
            height_count[heights[i]] += 1
            names_map[heights[i]] = names[i]
        
        res = []
        for i in range(high, -1, -1):
            if height_count[i]:
                res.append(names_map[i])

        return res