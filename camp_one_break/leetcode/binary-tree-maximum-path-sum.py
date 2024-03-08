# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        def depth_first_traverse(root):
            if not root:
                return(0, float('-inf')) 
            
            left = depth_first_traverse(root.left)
            right = depth_first_traverse(root.right)

            max_path = max(left[0], right[0])
            max_curr = max(root.val, max_path + root.val)

            max_path_sum = max(left[1], right[1], max(left[0] + right[0] + root.val, left[0] + root.val, right[0] + root.val, root.val))
            
            # returns (maximum path sum including itself and maximum path sum found till now or result)
            return (max_curr, max_path_sum)
        
        return depth_first_traverse(root)[1]
