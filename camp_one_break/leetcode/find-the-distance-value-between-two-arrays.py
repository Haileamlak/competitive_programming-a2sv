class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for num in arr1:
            if bisect_right(arr2, num + d) == bisect_left(arr2, num - d):
                res += 1
        
        return res