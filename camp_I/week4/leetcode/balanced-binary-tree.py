# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return (True, 0)
            
            left_height = helper(root.left)
            right_height = helper(root.right)

            return (left_height[0] and right_height[0] and abs(left_height[1] - right_height[1]) <= 1, max(left_height[1], right_height[1]) + 1)
        
        return helper(root)[0]