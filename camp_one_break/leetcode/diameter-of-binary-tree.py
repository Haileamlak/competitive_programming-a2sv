# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def depth_first_traverse(root):
            if not root:
                return (0, 0)
            
            left = depth_first_traverse(root.left)
            right = depth_first_traverse(root.right)

            height = max(left[0], right[0]) + 1
            diameter = max(left[1], right[1], left[0] + right[0])
            return (height, diameter)
        
        return depth_first_traverse(root)[1]