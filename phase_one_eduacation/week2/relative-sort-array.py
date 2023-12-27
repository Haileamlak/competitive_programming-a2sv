class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        high = max(arr1)
        arr_count = [0 for _ in range(high + 1)]

        for num in arr1:
            arr_count[num] += 1

        res = []            
        for num in arr2:
            while arr_count[num] > 0:
                res.append(num)
                arr_count[num] -= 1
                
        for num in range(high + 1):
            while arr_count[num] > 0:
                res.append(num)
                arr_count[num] -= 1
                
        return res