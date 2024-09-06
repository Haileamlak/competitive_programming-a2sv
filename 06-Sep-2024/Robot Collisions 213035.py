# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        robots.sort()

        stack = [robots[0]]
        for i in range(1, n):
            curr = robots[i]
            destroyed = False
            while stack and curr[2] == "L" and stack[-1][2] == "R":
                if curr[1] == stack[-1][1]:
                    stack.pop()
                    destroyed = True
                    break

                elif stack[-1][1] < curr[1]:
                    stack.pop()
                    curr[1] -= 1
                else:
                    stack[-1][1] -= 1
                    destroyed = True
                    break

            if not destroyed:
                stack.append(curr)

        return [x[1] for x in sorted(stack, key = lambda x : x[3])]