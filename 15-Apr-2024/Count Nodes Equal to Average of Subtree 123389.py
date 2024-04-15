# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0, 0)
            
            left_sum, left_n, left_res = dfs(node.left)
            right_sum, right_n, right_res = dfs(node.right)

            curr_sum = left_sum + right_sum + node.val
            n = left_n + right_n + 1

            res = left_res + right_res

            if node.val == curr_sum // n:
                res += 1
            
            return (curr_sum, n, res)

        return dfs(root)[2]