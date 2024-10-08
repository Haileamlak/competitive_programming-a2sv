# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for j in range(n)] for i in range(m)] 

        curr = head
        row, col = 0, 0
        while curr:
            for j in range(col, n):
                if curr:
                    matrix[row][j] = curr.val
                    curr = curr.next
                else:
                    break
            
            for i in range(row + 1, m):
                if curr:
                    matrix[i][n - 1] = curr.val
                    curr = curr.next
                else:
                    break

            for j in range(n - 2, col - 1, -1):
                if curr:
                    matrix[m - 1][j] = curr.val
                    curr = curr.next
                else:
                    break

            for i in range(m - 2, row, -1):
                if curr:
                    matrix[i][col] = curr.val
                    curr = curr.next
                else:
                    break
                
            n -= 1
            m -= 1
            row += 1
            col += 1
        
        return matrix