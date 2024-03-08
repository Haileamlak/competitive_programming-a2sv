# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def depth_first_traverse(root, curr_sum):
            if not root:
                return
            
            curr_sum += root.val
            path.append(root.val)

            if not root.left and not root.right and curr_sum == targetSum:
                    res.append(path.copy())
            
            depth_first_traverse(root.left, curr_sum)
            depth_first_traverse(root.right, curr_sum)

            path.pop()
            curr_sum -= root.val
        
        depth_first_traverse(root, 0)
        return res