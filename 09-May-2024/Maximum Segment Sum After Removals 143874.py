# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = {}
        _sum = {}

        def get(x):
            root = x
            while root != parent[root]:
                root = parent[root]
            
            while x != parent[x]:
                x, parent[x] = parent[x], root
            
            return x
        
        def union(x, y):
            px, py = get(x), get(y)

            parent[px] = py
            _sum[py] += _sum[px]

        _max = 0
        res = [0]

        for i in range(n - 1, 0, -1):
            u = removeQueries[i]
            parent[u] = u
            _sum[u] = nums[u]

            if u - 1 in parent:
                union(u - 1, u)
            
            if u + 1 in parent:
                union(u + 1, u)
            
            _max = max(_max, _sum[get(u)])
            
            res.append(_max)

        return reversed(res)