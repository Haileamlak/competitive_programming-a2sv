class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = [-1] * len(intervals)

        
        temp1 = [(intervals[i], i) for i in range(len(intervals))]
        temp1.sort(key = lambda x : x[0][1])

        temp2 = [(intervals[i], i) for i in range(len(intervals))]
        temp2.sort(key = lambda x : x[0][0])
        
        ptr2 = 0
        for ptr1 in range(len(temp1)):
            while ptr2 < len(intervals) and temp1[ptr1][0][1] > temp2[ptr2][0][0]:
                ptr2 += 1
            
            if ptr2 < len(temp2):
                res[temp1[ptr1][1]] = temp2[ptr2][1]
            else:
                break

        return res