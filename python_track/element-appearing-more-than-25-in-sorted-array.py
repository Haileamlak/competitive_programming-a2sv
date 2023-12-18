class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                if count > len(arr) // 4:
                    return arr[i - 1]
                count = 0
            count += 1

        return arr[-1]