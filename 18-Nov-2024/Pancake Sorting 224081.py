# Problem: Pancake Sorting - https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        index_map = {arr[i]: i for i in range(n)}
        
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                index_map[arr[start]] = start
                index_map[arr[end]] = end
                start += 1
                end -= 1

        res = []
        temp = list(sorted(arr, reverse=True))
        for i in range(n):
            k = index_map[temp[i]]
            res.append(k + 1)
            res.append(n - i)

            reverse(0, k)
            reverse(0, n - i - 1)

        return res