# Problem: Race Car - https://leetcode.com/problems/race-car/description/

class Solution:
    def racecar(self, target: int) -> int:
        res = 0
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        while queue:
            
            for _ in range(len(queue)):
                position, speed = queue.popleft()
                if position == target:
                    return res
                
                # accelerate
                acc_position = position + speed
                acc_speed = speed * 2
                if (acc_position, acc_speed) not in visited:
                    visited.add((acc_position, acc_speed))
                    queue.append((acc_position, acc_speed))
                
                
                
                # reverse
                rev_speed = -1 if speed > 0 else 1
                if (position, rev_speed) not in visited:
                    visited.add((position, rev_speed))
                    queue.append((position, rev_speed))
                
                if (position, rev_speed) in visited:
                    print('here')
            
            res += 1

        return 0