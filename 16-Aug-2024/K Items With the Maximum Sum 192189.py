# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        if numOnes >= k:
            return k

        res += numOnes
        k -= numOnes

        if numZeros >= k:
            return res

        k -= numZeros

        res -=  min(numNegOnes, k)
        
        return res