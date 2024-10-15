# Problem: Sum of Subarray minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        arr.append(0) 
        stack = [(0, -1)]
        for i in range( len(arr)):
            while stack and arr[i] < stack[-1][0]:
                res += stack[-1][0] * (stack[-1][1] - stack[-2][1]) * (i - stack[-1][1])
                stack.pop()

            stack.append((arr[i], i))

        return res % (pow(10, 9) + 7)