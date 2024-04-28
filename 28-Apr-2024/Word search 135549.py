# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        res = False
        visited = set()

        def back_track(i, j, index):
            nonlocal res
            if res:
                return
                
            if index == len(word):
                res = True
                return

            if ((i, j) in visited) or (i < 0 or i >= m) or (j < 0 or j >= n):
                return

            if board[i][j] != word[index]:
                return
            
            visited.add((i, j))
            back_track(i + 1, j, index + 1)
            back_track(i, j + 1, index + 1)
            back_track(i - 1, j, index + 1)
            back_track(i, j - 1, index + 1)
            visited.remove((i, j))
        
        for i in range(m):
            if res:
                break
            for j in range(n):
                if res:
                    break
                back_track(i, j, 0)

        return res