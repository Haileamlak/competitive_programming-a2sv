# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def get_height(root):
            if not root:
                return 0
            
            return max(get_height(root.left), get_height(root.right)) + 1
        
        height = get_height(root) - 1

        m = height + 1
        n = pow(2, height + 1) - 1

        res = [[''] * n for _ in range(m)]

        def traverse(root, row, col):
            if not root:
                return
            
            res[row][col] = str(root.val)
            
            x = pow(2, height - row - 1)

            traverse(root.left, row + 1, col - x)
            traverse(root.right, row + 1, col + x)
        
        traverse(root, 0, (n - 1) // 2)
        return res