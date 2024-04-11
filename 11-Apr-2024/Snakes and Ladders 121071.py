# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def position(num):
            r = ((num - 1) // n)
            c = (num - 1) % n
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c

            return row, col

        end = n * n

        visited = [False] * end
        visited[0] = True
        queue = deque([1])
        moves = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr == end:
                    return moves
                
                for next_move in range(curr + 1, min(curr + 6, end) + 1):
                    row, col = position(next_move)
                    if board[row][col] != -1:
                        next_move = board[row][col]

                    if not visited[next_move - 1]:
                        visited[next_move - 1] = True
                        queue.append(next_move)
            
            moves += 1
        
        return -1