# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted([-x[1] for x in nlargest(k, [(-abs(arr[i] - x), -arr[i]) for i in range(len(arr))])]) 