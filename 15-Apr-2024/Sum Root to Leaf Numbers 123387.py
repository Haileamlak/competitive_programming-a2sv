# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def traverse(root, curr):
            nonlocal res
            
            curr *= 10
            curr += root.val

            if not root.left and not root.right:
                res += curr
                return

            if root.left:
                traverse(root.left, curr)
                
            if root.right:
                traverse(root.right, curr)

        traverse(root, 0)
        
        return res