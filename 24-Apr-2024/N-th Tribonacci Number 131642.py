# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1:
            return n

        queue = deque([0, 1, 1])

        i = 3
        while i <= n:
            queue.append(sum(queue))
            queue.popleft()
            i += 1
        
        return queue.pop()