# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = []
        res = 0

        def traverse(root):
            nonlocal stack, res
            stack.append(str(root.val))
            if not root.left and not root.right:
                res += int(''.join(stack))
                stack.pop()
                return
                
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)

            stack.pop()
        
        traverse(root)
        
        return res