class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)

        
        temp1 = [(intervals[i], i) for i in range(len(intervals))]
        temp1.sort(key = lambda x : x[0][0])
        
        for i in range(len(res)):
            left, right = 0, len(intervals) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if temp1[mid][0][0] < intervals[i][1]:
                    left = mid + 1
                
                elif temp1[mid][0][0] > intervals[i][1]:
                    right = mid - 1
                else:
                    left = mid
                    break
            
            if left < len(intervals):
                res[i] = temp1[left][1]
        
        return res