class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # arr.sort()
        # arr[0] = 1

        # for i in range(len(arr)):
        #     if arr[i] - arr[i - 1] > 1:
        #         arr[i] = arr[i - 1] + 1
            
        # return arr[-1]

        surples = 0
        count = defaultdict(int)
        for elem in arr:
            if elem > len(arr):
                surples += 1
            else:
                count[elem] += 1
            
        res = len(arr)
        for i in range(len(arr), 0, -1):
            if i in count:
                surples += count[i] - 1

            else:
                if surples:
                    surples -= 1    
                else:
                    res -= 1

        return res            