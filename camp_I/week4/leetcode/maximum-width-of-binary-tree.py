# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = {}

        def traverse(root, row, col):
            if not root:
                return 
            
            if row not in answer:
                answer[row] = [col, col]
            else:
                answer[row][0] = min(answer[row][0], col)
                answer[row][1] = max(answer[row][1], col)
            
            if root.left:
                traverse(root.left, row + 1, 2 * col)
            
            if root.right:
                traverse(root.right, row + 1, 2 * col + 1)
        
        traverse(root, 0, 1)
        
        res = 0
        for row_range in answer.values():
            left_end = row_range[0]
            right_end = row_range[1]
            res = max(res, right_end - left_end + 1)
        
        return res