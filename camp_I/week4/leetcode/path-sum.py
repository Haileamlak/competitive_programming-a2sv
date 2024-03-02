# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def private_has_path_sum(root, curr_sum):

            curr_sum += root.val

            if not root.left and not root.right:
                if curr_sum == targetSum:
                    return True
                return False

            if root.left and private_has_path_sum(root.left, curr_sum):
                return True
            if root.right and private_has_path_sum(root.right, curr_sum):
                return True
            return False
        
        return private_has_path_sum(root, 0)