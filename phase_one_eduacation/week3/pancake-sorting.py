class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse(arr):
            i = 0
            n = len(arr)
            while i < n//2:
                arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
                i += 1
                
            return arr

        res = []
        n = len(arr)
        for i in range(n, 1, -1):
            arr = arr[:i]

            k = arr.index(max(arr))
            res.append(k + 1)
            res.append(i)

            arr = reverse(arr[:k + 1]) + arr[k + 1:]
            arr = reverse(arr)
        
        return res
