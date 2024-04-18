# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        temp = [(abs(arr[i] - x), arr[i]) for i in range(len(arr))]
        
        heapify(temp)

        res = []
        while k:
            curr = heappop(temp)[1]
            res.append(curr)
            k -= 1

        return sorted(res) 