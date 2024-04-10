# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        _dead_ends = set(deadends)

        if '0000' in _dead_ends:
            return -1
            
        res = float('inf')

        queue = deque([[[0, 0, 0, 0], 0]])
        visited = set(['0000'])

        while queue:
            curr, turns = queue.popleft()
            if ''.join([str(ch) for ch in curr]) == target:
                res = min(res, turns)
            else:
                for i in range(4):
                    temp = curr[i]

                    curr[i] = (temp + 1) % 10
                    temp1 = ''.join([str(ch) for ch in curr])
                    if temp1 not in _dead_ends and temp1 not in visited:
                        visited.add(temp1)
                        queue.append([curr.copy(), turns + 1])

                    curr[i] = (temp - 1) % 10
                    temp2 = ''.join([str(ch) for ch in curr])
                    if temp2 not in _dead_ends and temp2 not in visited:
                        visited.add(temp2)
                        queue.append([curr.copy(), turns + 1])

                    curr[i] = temp
        
        return res if res < float('inf') else -1