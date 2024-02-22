class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []
        for i in range(2 * n):
            while stack and stack[-1][0] < nums[i % n]:
                index = stack[-1][1]
                answer[index] = nums[i % n]
                stack.pop()

            stack.append((nums[i % n], i % n))
        
        return answer