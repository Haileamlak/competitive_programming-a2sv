# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)

        starting_combination = '0000'
        if starting_combination in visited:
            return -1
        
        visited.add(starting_combination)
        queue = deque([starting_combination])
        turns = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == target:
                    return turns

                temp = list(curr)
                for i in range(4):
                    curr_slot = int(temp[i])

                    temp[i] = str((curr_slot + 1) % 10)

                    next_state1 = ''.join(map(str, temp))
                    if next_state1 not in visited and next_state1 not in visited:
                        visited.add(next_state1)
                        queue.append(next_state1)

                    temp[i] = str((curr_slot - 1) % 10)

                    next_state2 = ''.join(map(str, temp))
                    if next_state2 not in visited and next_state2 not in visited:
                        visited.add(next_state2)
                        queue.append(next_state2)

                    temp[i] = str(curr_slot)
            
            turns += 1

        return -1