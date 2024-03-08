# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def depth_first_traverse(root, am_i_left):
            if not root:
                return 0
            
            if not root.left and not root.right and am_i_left:
                return root.val
            
            return depth_first_traverse(root.left, True) + depth_first_traverse(root.right, False)

        return depth_first_traverse(root, False)