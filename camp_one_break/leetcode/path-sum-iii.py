# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        res = 0

        def depth_first_traverse(root, curr_sum):
            nonlocal res
            if not root:
                return

            curr_sum += root.val
            res += sums[curr_sum - targetSum]
            
            sums[curr_sum] += 1

            depth_first_traverse(root.left, curr_sum)
            depth_first_traverse(root.right, curr_sum)

            sums[curr_sum] -= 1
            curr_sum -= root.val
        
        depth_first_traverse(root, 0)
        return res            