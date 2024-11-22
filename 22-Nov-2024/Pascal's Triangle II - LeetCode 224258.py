# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]

        rowBefore = self.getRow(rowIndex - 1)

        res = [1] * (rowIndex + 1)
        for i in range(1, rowIndex):
            res[i] = rowBefore[i - 1] + rowBefore[i]
        
        return res