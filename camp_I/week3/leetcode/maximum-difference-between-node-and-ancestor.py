# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        v = float('-inf')

        def traverse(root, minimum, maximum):
            if not root:
                return
            nonlocal v
            v = max(v, abs(root.val - minimum), abs(root.val - maximum))

            minimum = min(minimum, root.val)
            maximum = max(maximum, root.val)

            traverse(root.left, minimum, maximum)
            traverse(root.right, minimum, maximum)
        
        traverse(root, root.val, root.val)

        return v